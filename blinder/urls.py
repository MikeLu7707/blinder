from django.urls import path
from . import views

app_name = 'blinder'
urlpatterns = [
    path('book_list/', views.book_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
    path('',views.post_list, name = "home"),
    path('login/', views.loginView, name="login"),
    path('profile/', views.profileView, name="profile"),
    path('logout/', views.logoutView, name="logout"),
    path('contact/', views.displayContact),
]