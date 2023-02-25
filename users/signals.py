from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# The sender will be the user model. The user model will send a 
# signal everytime a new user is created that signal must have a 
# receiver. (see receiver function below.)

# The reciever will perfrom a task. in this case create a pofile.
# (see receiver func below)

# The arguments (sender, instance, created, **kwargs) in the create_user_profile func are coming from 
# the post_save signal.

# instance is an instance of the user model 
# create is a boolean (we are saying created is true)
# i added =True but it is not needed
# we are basically saying if a new user is created then 
# once it's saved we want to create a profile for the user. 
# THIS IS HOW A NEW PROFILE IS AUTOMATICALLY CREATED


# Receiver Function (a receiver func can be any python function or method)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(seller = instance)
        
        # once the profile is created we need to save it.
 
#saving the user profile        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
    #  ** MUST BE REGISTERED IN THE APPS.PY FILE ** #
    #  THIS WILL OVERIDE THE BUILT IN ready() method
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                # Django Signals
     # https://docs.djangoproject.com/en/4.1/topics/signals/
        # Django includes a “signal dispatcher” which helps decoupled
        # applications get notified when actions occur elsewhere in the 
        # framework. In a nutshell, signals allow certain senders to 
        # notify a set of receivers that some action has taken place.
        # They’re especially useful when many pieces of code may be 
        # interested in the same events.