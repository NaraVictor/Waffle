from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.


def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                con = Contact()
                con.email = request.POST['email']
                con.name = request.POST['name']
                con.message = request.POST['message']
                con.phone = request.POST['phone']
                con.save()
                return JsonResponse({'msg': 'Message sent'}, status=200)
            else:
                return JsonResponse({'msg': 'Required data missing'}, status=400)

        else:
            return render(request, 'contact/contact.html')
    except Exception as e:
        return JsonResponse({'msg': 'Oops, something bad happened!'}, status=400)
        # return JsonResponse({'msg': str(e)}, status=400)
