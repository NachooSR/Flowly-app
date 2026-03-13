from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,"core/landing.html")

def about_us(request):
    return render(request,"core/about.html")

def appMode(request):
    return render(request,"core/appmode.html")