from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.authentication.models import POSUser

# Register your models here.
admin.site.register(POSUser)