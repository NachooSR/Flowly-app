from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionExpenseForm,TransactionIncomeForm
from .models import Transaction



@login_required
def home(request):

    date_query = request.GET.get("date")

    transactions = Transaction.objects.filter(user=request.user)

    if date_query:
        transactions = transactions.filter(transaction_date=date_query)

    transactions = transactions.order_by("-transaction_date")

    return render(
        request,
        "transactions/home.html",
        {"transactions": transactions}
    )

@login_required
def create_income(request):

    form = TransactionIncomeForm(request.POST or None) 
    if request.method == "POST" and form.is_valid():
        transaction=  form.save(commit=False)
        transaction.user = request.user
        transaction.type = "income"
        transaction.save()
        return redirect("home")

    return render(request, "transactions/create_income.html", {"form": form})

@login_required
def create_expense(request):

    form = TransactionExpenseForm(request.POST or None) 
    if request.method == "POST" and form.is_valid():
        transaction=  form.save(commit=False)
        transaction.user = request.user
        transaction.type = "expense"
        transaction.save()
        return redirect("home")

    return render(request, "transactions/create_expense.html", {"form": form})

@login_required
def edit_transaction(request, id):

    transaction = Transaction.objects.get(
        id=id,
        user=request.user
    )

    if transaction.type == "income":
        form_class = TransactionIncomeForm
    else:
        form_class = TransactionExpenseForm

    form = form_class(request.POST or None, instance=transaction)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")

    return render(
        request,
        "transactions/edit.html",
        {"form": form}
    )


@login_required
def delete_transaction(request,id):
    
    transaction= Transaction.objects.get(   id=id,
        user=request.user
    )
    transaction.delete()
    return redirect('home')
    

