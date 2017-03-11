from django.db import models
from vote.models import VoteModel
from steewi.users.models import User
import datetime

class Product(VoteModel, models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.slug)])

    def get_recent_comments_list(self):
        last_day_begins = datetime.datetime.now() - datetime.timedelta(days=1)
        return self.productcomment_set.filter(created_at__gte=last_day_begins).all()


class ProductComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    author_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)





