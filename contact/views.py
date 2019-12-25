from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.


def contact(request):
    # try:
    if request.method == 'POST':
        # print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            con = Contact(request.POST)
            print('got here')
            con.save()
            return JsonResponse({'msg': 'Data received successfully'}, status=200)
        else:
            return JsonResponse({'msg': 'Data is not valid'}, status=400)

    else:
        form = ContactForm()
        return render(request, 'contact/contact.html',
                      {
                          'form': form,
                      })
    # except Exception as e:
    # # return JsonResponse({'msg': 'Oops, something really bad happened!'}, status=400)
    # return JsonResponse({'msg': str(e)}, status=400)
