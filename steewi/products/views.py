from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import JsonResponse

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
        context['ordering_options'] = ('name', 'vote_score')
        return context

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        if user.id is not None:
            context['current_user_voted'] = product.votes.exists(user.id)
        else:
            context['current_user_voted'] = False
        return context


def like(request, user_id, product_id):
    product = Product.objects.get(pk=product_id)
    product.votes.up(user_id)
    return JsonResponse({'result': 'ok'})
