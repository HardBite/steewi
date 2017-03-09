from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductList(ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        order = self.request.GET.get('order_by', 'name')
        new_context = Product.objects.order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['order_by'] = self.request.GET.get('order_by', 'name')
        context['ordering_options'] = ('name',)
        return context

class ProductDetail(DetailView):
    model = Product
