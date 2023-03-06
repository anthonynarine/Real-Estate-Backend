from rest_framework import serializers
from users.models import Profile
from listings.models import Listing
from listings.serializers import ListingSerializer


# this class will inherit from serializers.ModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
    seller_listings = serializers.SerializerMethodField()
    
    def get_seller_listings(self, obj):
    # we want the seller on the listing to be = to the seller on the serialize obj.     
        query = Listing.objects.filter(seller=obj.seller)
        listings_serialized = ListingSerializer(query, many=True)
        # print(listings_serialized.data)
        return listings_serialized.data
    # without the .data an object will be returned and throw an error check on postman w/ .data off
        
    class Meta:
        model = Profile
        fields = "__all__"
        print(Profile)
        
        
        
        #DONT FORGET TO CREATE A VIEW FOR THIS 