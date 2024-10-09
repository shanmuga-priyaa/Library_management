from django.urls import path
from .views import *

urlpatterns = [
    path('transactionadd/', TransactionAddView.as_view()),
    path('transactionlist/', TransactionListView.as_view()),
]