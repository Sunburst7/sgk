from django.contrib import admin

# Register your models here.
from .models import Group,Account

admin.site.register(Group)
admin.site.register(Account)