from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

 
# Create your views here.
def signin(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is None:
            return render(request, "users/signin.html", {
                "form": AuthenticationForm(),
                "error": "Email or password is incorrect"
            })

        login(request, user)
        return redirect("home")

    return render(request, "users/signin.html", {
        "form": AuthenticationForm()
    })

def register(request):

    form = CustomUserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user= form.save()
        login(request,user)
        
        return redirect("home")

    return render(request, "users/register.html", {"form": form})

def signout(request):
    logout(request)
    return redirect('landing')