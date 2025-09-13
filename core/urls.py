from django.urls import path
from . import views
from .views import api_root, login, signup, UpdateLocationView, GetLocationView
from core import views

urlpatterns = [
    path('api/', api_root,name='api_root'),
    path('', views.home, name='home'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("update-location/", UpdateLocationView.as_view(), name="update-location"),
    path("get-location/", GetLocationView.as_view(), name="get-location"),

]

