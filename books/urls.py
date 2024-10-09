from django.urls import path
from .views import BookAddView, BookListView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('bookadd/', BookAddView.as_view(), name='bookadd'),
    path('booklist/', BookListView.as_view(), name='booklist'),
    path('bookupdate/<int:id>/', BookUpdateView.as_view(), name='book_update'),
    path('bookdelete/<int:id>/', BookDeleteView.as_view(), name='book_delete'),
]
