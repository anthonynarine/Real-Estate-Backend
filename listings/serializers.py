from rest_framework import serializers
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):  
    # the fild you want to add is alway set up with the name of the field then serializers.SerializerMethodField() 
    state = serializers.SerializerMethodField() 
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()

    
    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name
        
    def get_seller_username(self, obj):
        return obj.seller.username
         
#self is an instance of the class object and obj is the serialize data obj.
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
#    by convension the name of the function is will starrt with get_ 
#    by underscore then the field name (seeabove)

# 3. the function will take two arguments self and obj.    
    # self is as always is an instance of the calss object
    # ojb is the serialized data object. in this example
    # we wont need the arugments. 
    # by returning "New York" we added a new field called state
    # to our serialized object
    
    
    
#     SerializerMethodField
# This is a read-only field. It gets its value by calling a method on the serializer class it is attached to. It can be used to add any sort of data to the serialized representation of your object.

# Signature: SerializerMethodField(method_name=None)

# method_name - The name of the method on the serializer to be called. If not included this defaults to get_<field_name>.
# The serializer method referred to by the method_name argument should accept a single argument (in addition to self), which is the object being serialized. It should return whatever you want to be included in the serialized representation of the object. For example:

# from django.contrib.auth.models import User
# from django.utils.timezone import now
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = '__all__'

#     def get_days_since_joined(self, obj):
#         return (now() - obj.date_joined).days