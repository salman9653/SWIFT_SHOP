from django.contrib import admin
from .models import User,Profile
from django.contrib.auth.models import Group


admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Profile)
