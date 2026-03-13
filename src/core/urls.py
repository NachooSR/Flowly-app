from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('about_us',views.about_us,name="about_us"),
    path('appMode',views.appMode,name="appMode")
]