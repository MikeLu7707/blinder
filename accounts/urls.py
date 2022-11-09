from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.registerView, name="signup"),
    path('<pk>/upadte', views.UserEditView.as_view(), name="editProfile")
]