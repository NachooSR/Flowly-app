from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, AccountType


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "type_account",
            "password1",
            "password2"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields["type_account"].choices = AccountType.choices

        
        balance_value = AccountType.BALANCE
        self.fields["type_account"].widget.choices = [
            (value, label if value != balance_value else f"{label} (Coming soon)")
            for value, label in AccountType.choices
        ]
        
    def clean_type_account(self):
        value = self.cleaned_data.get("type_account")

        if value == AccountType.BALANCE:
            raise forms.ValidationError("Balance mode is still in development.")

        return value