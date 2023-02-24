from django.contrib import admin
from .models import Profile
#syntax Django need for User app import 
from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(User)
admin.site.register(Profile)
