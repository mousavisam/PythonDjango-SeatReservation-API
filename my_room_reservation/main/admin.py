from django.contrib import admin
from .model.user_entity import User
from .model.account_entity import Account


# Register your models here.
admin.site.register(User)
admin.site.register(Account)
