from django.contrib import admin

#syntax Django need for User app inport 
from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(User)
