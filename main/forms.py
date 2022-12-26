from .models import *
from django.forms import EmailInput, ModelForm, TextInput


class MainForm(ModelForm):
    class Meta:
        model = main
        fields = ["first_name", "second_name", "phonenumber", "email"]
        widgets = {

            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',

            }),

            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'

            }),

            "email": EmailInput(attrs={
                'class': 'form-controle',
                'placeholder': 'Введите email',

            }),

            "phonenumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'

            }),

        }
