# from django import forms
# from .models import Listing
# from django.contrib.gis.geos import Point

# #       NOTE  this from must be registered in admin.py

#                 #  FORM FUNCTIONALITY START  #          

# class ListingsForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         fields = "__all__"
#         extra_fields = ["latitude", "longitude", "picture1", "picture2", "picture3", "picture4", "picture5",]

#     latitude = forms.FloatField()
#     longitude = forms.FloatField()

# # CLEAN Method allows us to perform some logic and manipulate the form
# # The super() method allows us access to the form itself.
# # Data is a dictionalry with key:value pair we extract into
# # latitude and longitude variables that are used above as the forms.floatfield.
#     def clean(self):
#         data = super().clean()
#         latitude = data.pop("latitude")
#         longitude = data.pop("longitude")
#         data["location"] = Point(latitude, longitude, srid=4326)
#         return data

# #   NOTE this code will overide the init form method. without the overide
# #        the entered latitude and longitude in the form will disapear
# #        The location will be marked on the map but we want to show the
# #         entered latitude and longitude in the form 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         location = self.initial.get("location")
#         if isinstance(location, Point):
#             self.initial["latitude"] = location.tuple[0]
#             self.initial["longitude"] = location.tuple[1]
            
            
                #  FORM FUNCTIONALITY END #          
            
            

# The super() method allows  acces to the form. the super method
# is initialized with the .__init__(...)
# Location is a Point field and point fields have a property called tuple
# tuple returns the coordinates of a Point as a tuple
# The if statement check if location is an instance if thats the case
# we return latitiude and logitude from their index as show

            # "__all__" magic method explained
            # NOTE this list of fields from Listing is easily added with "__al__"
            # magic method
        #  fields = ["title", "description", "area", "listing_type", "property_status", "price", "rental_frequency",
        #           "rooms", "furnished", "pool", "elevator", "parking", "date_posted", "location", "location",
        #           "latitude", "longitude"]

        # NOTE the syntax above to add additional fields

        # NOTE Clean method allows us to perform some logic and manipulate the form
        #         def clean(self):
        #             data = super().clean
        #   The super() method allows access to the form itself the
        #   The data variable will be dictionary with key:value pairs
        #   We needed the location field from the latitude and longitude
        #   fields + it has to be a point object

        #                   NOTE SRID
        # Every geometric shape has a spatial reference system associated
        # with it, and each such reference system has a Spatial Reference
        # System ID (SRID). The SRID is used to tell which spatial reference
        # system will be used to interpret each spatial object.

        # A common SRID in use is 4326, which represents spatial data
        # using longitude and latitude coordinates on the Earth's surface
        # as defined in the WGS84 standard, which is also used for the Global
        # Positioning System (GPS)
