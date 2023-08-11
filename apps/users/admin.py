from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User
# Register your models here.

admin.site.register(User)
admin.site.unregister(User)
admin.site.unregister(Group) 