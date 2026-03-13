from django.urls import path
from .import views

urlpatterns = [
    path('signin',views.signin,name="singing"),
    path('register',views.register,name="register"),
    path('logout/',views.signout,name="logout")
]