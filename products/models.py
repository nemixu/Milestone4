from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Model to define the category name and friendly name
    """
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True,)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Return a friendly name to ensure easier readability in admin"""
        return self.friendly_name


class Product(models.Model):
    """
    Model defined for each product in the database
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model to define the fields required to add a review to a product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name="reviews")
    comment = models.TextField(max_length=1000, blank=True, null=True)
    rating = models.FloatField(default=1)

    def __str__(self):
        return self.user.username
    