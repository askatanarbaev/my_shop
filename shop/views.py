from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic import View
from django.views.generic import DetailView, FormView
from cart.forms import CartAddProductForm
from django.views.generic import View


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context 


class CategoryListView(ListView):
    model = Product
    context_object_name = 'cat_prod'
    template_name = 'cat_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context 

class CategoryListView2(ListView):
    model = Product
    context_object_name = 'cat_prod2'
    template_name = 'cat_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView2, self).get_context_data(**kwargs)
        return context 


class ProductDetailView(DetailView):
    
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
            context = super(ProductDetailView, self).get_context_data(**kwargs)
            context['cart_product_form'] = CartAddProductForm
            return context
