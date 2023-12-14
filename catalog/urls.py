from django.urls import path

from catalog.views import index, homepage, contacts

urlpatterns = [
    path('', homepage),
#    path('home/', homepage),
    path('contact/', contacts)
]
