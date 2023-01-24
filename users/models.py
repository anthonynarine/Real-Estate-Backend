from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#   User class inherits from above AbstractUser model
#   CHANGES to the User class must be reported to django in project settings
class User(AbstractUser):
    email = models.EmailField(unique=True)







#           Djagngo Abstract user
