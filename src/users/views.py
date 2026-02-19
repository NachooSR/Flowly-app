from django.shortcuts import render
from . import models
 
# Create your views here.
def home(request):
    profiles= models.Profile.objects.all()
    return render(request,"users/login.html",{"profiles": profiles})