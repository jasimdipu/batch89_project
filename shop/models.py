from django.db import models
from django.urls import reverse

# Create your models here.


class ProductManager(models.Manager):
    def get_query(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/category/')

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_path(self):
        return reverse('shop:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    descrioption = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/product/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_path(self):
        return reverse('shop:product_detail', args=[self.slug])

    def __str__(self):
        return self.name
