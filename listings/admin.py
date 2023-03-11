from django.contrib import admin
# from .models import Listing
from listings.models import Listing
from listings.models import Poi
from .forms import PoisForm

# NOTE in order to modify the form in the admin panel
#      we need to create a new admin class.

class PoiAdmin(admin.ModelAdmin):
    form = PoisForm


admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)