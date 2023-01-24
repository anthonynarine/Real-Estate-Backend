from django.shortcuts import render

# Create your views here.
from listings.serializers import ListingSerializer
from listings.models import Listing
from rest_framework import generics

#class based get all request.
class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    
    
    
    
