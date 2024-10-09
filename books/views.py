# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import BookForm 
# from .models import Book
# from django.contrib.auth.mixins import LoginRequiredMixin

# class BookAddView(View):
#     def get(self, request):
#         data = {"bookForm": BookForm()}
#         return render(request, 'bookadd.html', data)

#     def post(self, request):
#         new_data = BookForm(request.POST, request.FILES)
#         if new_data.is_valid():
#             new_data.save()
#         data = {"bookForm": new_data}
#         return render(request, 'bookadd.html', data)
# #__________________________________________________________________________
 
# class BookListView(LoginRequiredMixin,View):
#     login_url = '/'
#     def get(self,request):
#         data={"booklist":Book.objects.all()}
#         print(data)
#         return render(request,'Booklist.html',data)
# #___________________________________________________________________________

# class BookDeleteView(View):
#     def get (self,request,id):
#         selected_data = Book.objects.get(id=id)
#         selected_data.delete()
#         return  redirect ('/Book/Booklist/')
# #_________________________________________________________________________________

# class BookUpdateView(View):
#     def get(self,request,id):
#         selected_data = Book.objects.get(id=id)
#         data = {"bookForm":BookForm(instance=selected_data)}
#         return render(request,'Bookadd.html',data)
#     def post(self,request,id):
#         selected_data = Book.objects.get(id=id)
#         new_data=BookForm(request.POST,instance=selected_data)
#         if new_data.is_valid():
#             new_data.save()
#             return redirect('/Book/Booklist/')
# #__________________________________________________________________________________

from django.shortcuts import render, redirect
from django.views import View
from .forms import BookForm 
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

class BookAddView(View):
    def get(self, request):
        data = {"bookForm": BookForm()}
        return render(request, 'bookadd.html', data)

    def post(self, request):
        new_data = BookForm(request.POST, request.FILES)
        if new_data.is_valid():
            new_data.save()
            return redirect('/books/booklist/')  # Redirect to the book list after adding a book
        data = {"bookForm": new_data}
        return render(request, 'bookadd.html', data)

class BookListView(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request):
        data = {"booklist": Book.objects.all()}
        return render(request, 'Booklist.html', data)

class BookDeleteView(View):
    def get(self, request, id):
        selected_data = Book.objects.get(id=id)
        selected_data.delete()
        return redirect('/books/booklist/')  # Redirect to the book list after deletion

class BookUpdateView(View):
    def get(self, request, id):
        selected_data = Book.objects.get(id=id)
        data = {"bookForm": BookForm(instance=selected_data)}
        return render(request, 'bookadd.html', data)

    def post(self, request, id):
        selected_data = Book.objects.get(id=id)
        new_data = BookForm(request.POST, instance=selected_data)
        if new_data.is_valid():
            new_data.save()
            return redirect('/books/booklist/')  # Redirect to the book list after updating

