from django.shortcuts import render, redirect, get_object_or_404
from .forms import PetCreateForm
from .models import Pet
from django.views import generic
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Pet
    paginate_by = 3

class AddView(generic.CreateView):
    model = Pet
    form_class = PetCreateForm
    success_url = reverse_lazy('snake:index')

class UpdateView(generic.UpdateView):
    model = Pet
    form_class = PetCreateForm
    success_url = reverse_lazy('snake:index')

class DeleteView(generic.DeleteView):
    model = Pet
    success_url = reverse_lazy('snake:index')


class DetailView(generic.DetailView):
    model = Pet
