from django import forms
from django.forms import ModelForm
from .models import Transaction, Category


class TransactionIncomeForm(ModelForm):

    new_category = forms.CharField(
        required=False,
        label="New category"
    )

    class Meta:
        model = Transaction
        fields = [
            "name",
            "category",
            "amount",
            "payment_method",
            "nature",
            "transaction_date"
        ]

        widgets = {
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"step": "0.01"}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than 0")

        return amount

class TransactionExpenseForm(ModelForm):

    new_category = forms.CharField(
        required=False,
        label="New category"
    )

    class Meta:
        model = Transaction
        fields = [
            "name",
            "category",
            "recipient",
            "amount",
            "payment_method",
            "nature",
            "transaction_date"
        ]

        widgets = {
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"step": "0.01"}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than 0")

        return amount