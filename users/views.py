from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

#create a view and endpoint url for a list of all profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Create a view and endpoint url for evey profile
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "seller"
    
    



# DONT FORGET TO CREATE THE url FOR THIS VIEW IN PROJECT urls.py