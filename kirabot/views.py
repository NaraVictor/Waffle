import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer


class ChatterBotAppView(TemplateView):
    template_name = 'kirabot/kira.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    kira = ChatBot('Kira',
                   database_uri='sqlite:///kira.sqlite3',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   logic_adapters=[
                       {
                           'import_path': 'chatterbot.logic.BestMatch',
                           'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance'
                       },
                       {
                           'import_path': 'chatterbot.logic.MathematicalEvaluation'
                       },
                       # {
                       #     'import_path':'chatterbot.logic.TimeLogicAdapter'
                       # }
                   ],

                   # works just fine
                   # trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer',
                   # training_data = ['./customcorpus.yml','chatterbot.corpus.english','chatterbot.corpus.french']

                   )

    # trainer = ChatterBotCorpusTrainer(kira)
    # trainer.train('./customcorpus.yml',
    #               'chatterbot.corpus.english', 'chatterbot.corpus.french')

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.kira.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.kira.name
        })
