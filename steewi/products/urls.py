from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ProductList.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w-]+)/$',
        view=views.ProductDetail.as_view(),
        name='detail'
    ),
    url(
        regex=r'^like/(?P<user_id>[\d]+)/(?P<product_id>[\d]+)/$',
        view=views.like,
        name='like'
    ),
]
