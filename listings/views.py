from django.shortcuts import render

# Create your views here.
from listings.serializers import ListingSerializer
from listings.models import Listing
from rest_framework import generics


# class based get all request.
# This view will show all the property listings in JSON format
class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all().order_by(
        "-date_posted"
    )  # .order_by("-date_posted") will display listings from newest to oldest
    serializer_class = ListingSerializer

    # This view is responsibe for the POST REQUEST
    # used in  AddProperty from in the front end
class CreateListing(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    #add url for this view  - path("api/listings/create/", listings_views.CreateListing.as_view()), 

    # get request.
class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    #add url for this view -  path("api/listings/<int:pk>/", listings_views.ListingDetail.as_view()), 
    
class ListingDelete(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    #add url path for this view.
