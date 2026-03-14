from django.urls import path
from . import views

urlpatterns = [
     path('home',views.home,name="home"),
     path('createIncome',views.create_income,name="createIncome"),
     path('createExpense',views.create_expense,name="createExpense"),
     path("edit/<int:id>/", views.edit_transaction, name="edit_transaction"),
     path("delete/<int:id>/", views.delete_transaction, name="delete_transaction")
] 

