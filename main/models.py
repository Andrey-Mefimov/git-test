from django.db import models



class main(models.Model):
    first_name = models.CharField('Логин', max_length=15)
    second_name = models.CharField('Пароль', max_length=15)
    phonenumber = models.CharField('Номер',max_length=12, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Аккаунт участника'
        verbose_name_plural = 'Аккаунты участников'

