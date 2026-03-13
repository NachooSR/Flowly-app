from django.conf import settings
from django.db import models
from django.utils import timezone


# region Clases Aux
class Category(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class PaymentMethod(models.TextChoices):
    
    CASH = "cash", "Cash"
    WALLET = "wallet", "Wallet"
    CARD = "card", "Card"


class TransactionNature(models.TextChoices):
    
    FIXED = "fixed", "Fixed"
    VARIABLE = "variable", "Variable"

class TransactionType(models.TextChoices):
    
    EXPENSE = "expense", "Expense"
    INCOME = "income", "Income"



class Transaction(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    nature = models.CharField(max_length=10, choices=TransactionNature.choices)
    transaction_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)


'''
Id -> generado automaticamente (Lo hace solo la tabla)
Nombre-> (Opcional) 
Categoria-> (Opcional)
Destinario-> (Opcional -> lista conta/nombre)
Monto -> not null
forma pago -> efectivo, wallet..
Fijo o variable
fecha-> automatica/manual
'''

