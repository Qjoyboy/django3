from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def dop(request):
    return render(request, 'catalog/dop.html')


# --------------------------------------------
'''CBV для продукта'''


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'desc', 'image', 'category', 'price', 'create_date', 'last_change')
    success_url = reverse_lazy('catalog:home')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'desc', 'image', 'category', 'price', 'create_date', 'last_change')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
