from django.urls import path
from .views import displayContact
from .views import book_list, post_list, post_detail

app_name = 'blinder'
urlpatterns = [
    path("book_list/", book_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail' ),
    path('',post_list, name = "home")
    #path("contact/", displayContact),
]
 


