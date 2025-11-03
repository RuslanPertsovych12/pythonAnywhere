from django.shortcuts import render
from django.views import generic
from . import models

class BookView(generic.ListView):
    model = models.Book

class BookView(generic.DetailView):
    model = models.Book