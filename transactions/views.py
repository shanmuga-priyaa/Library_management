from django.shortcuts import render, redirect
from django.views import View
from .models import transaction
from .forms import transactionForm

class TransactionAddView(View):
    def get(self, request):
        data = {"transactionForm": transactionForm()}
        return render(request, 'transactionadd.html', data)

    def post(self, request):
        new_data = transactionForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect('/transactions/transactionlist/')
        return render(request, 'transactionadd.html', {'transactionForm': new_data})

class TransactionListView(View):
    def get(self, request):
        data = {"transactionlist": transaction.objects.all()}
        print(data)  # Optional: For debugging
        return render(request, 'transactionlist.html', data)
