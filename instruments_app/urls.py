from django.urls import path
from instruments_app import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='books_list'),
]