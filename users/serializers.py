from rest_framework import serializers
from users.models import Profile


# this class will inherit from serializers.ModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
        
        #DONT FORGET TO CREATE A VIEW FOR THIS 