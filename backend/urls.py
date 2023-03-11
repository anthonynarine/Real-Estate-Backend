"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Why did you do this
from listings import views as listings_views  
from users import views as users_views

# Serving files (images) uploaded by a user during development below imports needed
# Along with the + static [setting. as shown below]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/listings/", listings_views.ListingList.as_view()), 
    # posting property endpoint
    path("api/listings/create/", listings_views.CreateListing.as_view()), 
    path("api/listings/<int:pk>/", listings_views.ListingDetail.as_view()), 
    #since we well be accessing single profile we will access it by its pk NOTE the syntax 
    # its better to identify a profile by the id of the seller than with the id of the profile (pk)   
    # path("api/profiles/<int:pk>/", users_views.ProfileDetail.as_view()), 
    path("api/listings/<int:pk>/delete/", listings_views.ListingDelete.as_view()), 
    path("api/profiles/<int:seller>/", users_views.ProfileDetail.as_view()), 
    path("api/profiles/<int:seller>/update/", users_views.ProfileUpdate.as_view()),
    #This endpoint will be a get all profile view
    path("api/profiles/", users_views.ProfileList.as_view()),
     
    path("api-auth-djoser/", include('djoser.urls')),
    path("api-auth-djoser/", include('djoser.urls.authtoken')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static (settings..... is part of serving uploaded media files )
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# NOTE for class based view listings views is imported and named as listing_view
#      the path to that view is wiritten as shown above. 
#      view_name.class_name.as_view()
