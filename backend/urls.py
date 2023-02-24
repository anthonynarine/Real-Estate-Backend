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

# Serving files (images) uploaded by a user during development below imports needed
# Along with the + static [setting. as shown below]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/listings/", listings_views.ListingList.as_view()), 
    path("api/listings/create/", listings_views.CreateListing.as_view()), 
    # posting property endpoint
     
    path("api-auth-djoser/", include('djoser.urls')),
    path("api-auth-djoser/", include('djoser.urls.authtoken')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static (settings..... is part of serving uploaded media files )
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# NOTE for class based view listings views is imported and named as listing_view
#      the path to that view is wiritten as shown above. 
#      view_name.class_name.as_view()
