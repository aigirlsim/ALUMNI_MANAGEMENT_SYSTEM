from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Course)

admin.site.register(Session_Year)

admin.site.register(Alumni)

admin.site.register(Insitute)

admin.site.register(Contact)

admin.site.register(Event)

admin.site.register(PJob)