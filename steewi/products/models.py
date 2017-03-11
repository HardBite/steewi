from django.db import models
from vote.models import VoteModel
from steewi.users.models import User

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

# todo Test cascade deletion
class ProductComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
