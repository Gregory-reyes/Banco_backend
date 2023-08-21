from django.contrib import admin
from .models.account import Account
from .models.user import User
from authApp.models import user

from authApp.models import account

# Register your models here.
admin.site.register(User) #pilas puesssssssssssssssssssss con la mayuscula inicial
admin.site.register(Account) # tambien