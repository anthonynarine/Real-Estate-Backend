from rest_framework import serializers
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):  
    # the fild you want to add is alway set up with the name of the field then serializers.SerializerMethodField() 
    state = serializers.SerializerMethodField() 
    seller = serializers.SerializerMethodField()
        
    def get_seller_username(self, obj):
        return obj.seller_username.username   
         
    def get_state(self, obj):
        return "New York"
    class Meta:
        model= Listing
        fields = "__all__"


        
        
        
        

# adding a field to be serialized that is not on the app model.
# see above for code example named state.
# 1. the field is defined under the model serializer class and
#     is set = serializers.SerializerMethodField()
    
# 2. a function is defined with what we want declared on the field
#    by convension the name of the function is started with get followed
#    by underscore (seeabove)

# 3. the function will take two arguments self and obj.    
    # self is as always is an instance of the calss object
    # ojb is the serialized data object. in this example
    # we wont need the arugments. 
    # by returning "New York" we added a new field called state
    # to our serialized object