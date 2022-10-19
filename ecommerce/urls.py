from django.urls import path
from .views import item, MyView #added


urlpatterns = [
    path("", item),
    #path("", include("blinder.urls")),
    path('about/', MyView.as_view()) 
]