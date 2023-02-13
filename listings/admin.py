from django.contrib import admin
# from .models import Listing
from listings.models import Listing
# from .forms import ListingsForm

# NOTE in order to modify the form in the admin panel
#      we need to create a new admin class.

# class ListingAdmin(admin.ModelAdmin):
#     form = ListingsForm


admin.site.register(Listing)