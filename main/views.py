from django.shortcuts import render
from .forms import *
from .models import *

def index(request):
    form = MainForm()
    error = ''
    if request.method == 'POST':
        form = MainForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            form.save()
            error = 'Вы успешно зарегистировались =)'
            
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'

    context = {
            'form': form,
            'error': error,

        }

    return render(request, 'main/create.html', context)
