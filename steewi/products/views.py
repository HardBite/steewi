from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product, ProductComment
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
        context['ordering_options'] = {'name': "Name", 'vote_score': "Likes"}
        return context

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        comment_form = ProductCommentForm()
        if user.id is not None:
            context['current_user_voted'] = product.votes.exists(user.id)
            comment_form.fields['author_name'].widget.attrs['value'] = user.username
            comment_form.fields['author_name'].widget.attrs['readonly'] = True
        else:
            context['current_user_voted'] = False
        context['comment_form'] = comment_form
        return context

    def post(self, request, **kwargs):
        product = self.get_object()
        user = self.request.user
        form = ProductCommentForm(request.POST)
        comment = form.save(commit=False)
        if user.id is not None:
            comment.author = user
        comment.product = product
        comment.save()
        return redirect('/products/{}'.format(product.slug))

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['author_name', 'text']

    def __init__(self, *args, **kwargs):
        super(ProductCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['text'].widget.attrs['rows'] = 3
        self.helper.add_input(Submit('submit', 'Submit'))


def like(request, user_id, product_id):
    product = Product.objects.get(pk=product_id)
    product.votes.up(user_id)
    return JsonResponse({'result': 'ok'})
