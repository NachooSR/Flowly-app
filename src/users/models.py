from django.db import models
from django.contrib.auth.models import AbstractUser

class AccountType(models.IntegerChoices):
    TRACKING = 1,"Tracking"
    BALANCE = 2,"Balance"

# Create your models here.
class CustomUser (AbstractUser):
    
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    type_account = models.IntegerField(
        choices = AccountType.choices,
        default = AccountType.TRACKING 
    )
    
    balance = models.FloatField(default= 0)
    
    profile_image = models.ImageField(
        upload_to= "profiles/",
        null= True,
        blank= True
    )
    
