from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
       
    # overiding the ready method for signal registration 
    def ready(self):
        import users.signals
    
    
