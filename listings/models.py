from django.contrib.gis.db import models
from random import choices
from django.utils import timezone
from django.contrib.gis.geos import Point
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Listing(models.Model):
    # sellers and users are the same so the fk will point to the User model.
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    choices_area = (
        ("Brooklyn", "Brooklyn"),
        ("Queens", "Queens"),
        ("Bronx", "Bronx"),
        ("Manhattan", "Manhattan"),
        ("Statin Island", "Statin Island"),
    )
    area = models.CharField(max_length=25, blank=True, null=True, choices=choices_area)
    choices_listing_type = (
        ("House", "House"),
        ("Appartment", "Appartment"),
        ("Office", "Office"),
        ("Commercial space", "Commercial Space"),
        ("Parking Space", "Parking Space"),
    )
    listing_type = models.CharField(max_length=20, choices=choices_listing_type)
    choices_propery_status = (("Sale", "Sale"), ("Rent", "Rent"))
    property_status = models.CharField(
        max_length=25, blank=True, null=True, choices=choices_propery_status
    )
    price = models.DecimalField(max_digits=50, decimal_places=0)
    choices_rental_frequencey = (
        ("Month", "Month"),
        ("Week", "Week"),
        ("Day", "day"),
    )
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequencey
    )
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    # LOCATION FIELD FUNCTIONALIY Will be MOVED TO FRONT END
    # location = models.PointField(blank=True, null=True, srid=4326)
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture4 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture5 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")

    def __str__(self):
        return self.title

    # pipenv install pillow will allow us to use imageFields in Django.


#                   // Model   NOTE(s)\\

#                    choices field
# If choices are given, they’re enforced by
# model validation and the default form widget will be a select box with
# these choices instead of the standard text field. The first element in each
# tuple is the actual value to be set on the model, and the second element is
# the human-readable name. For example:

#                  #location field (PointField)
# GeoDjango helps create geographic web apps.
# PointField is a django GeoDjanogo field that stores a point which has a pair of coordinates.
# GEOS API >> import from django.contrib.gis.geos import Point

#                   geodjango installation
# spatial refrence identifier Srid


# ADD to project settings
# https://www.lfd.uci.edu/~gohlke/pythonlibs/  (GDAL Binaries)


# import os

# if os.name == 'nt':
#     VENV_BASE = os.environ['VIRTUAL_ENV']
#     os.environ['PATH'] = os.path.join(
#         VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
#     os.environ['PROJ_LIB'] = os.path.join(
#         VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']


# 2/5/23 adding the latitude and longitude functionality moved to front end.
