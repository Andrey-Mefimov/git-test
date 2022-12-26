from django.contrib import admin
from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'phonenumber', 'email')
    list_display_links = ('id', 'first_name', 'second_name')

admin.site.register(main, MainAdmin)