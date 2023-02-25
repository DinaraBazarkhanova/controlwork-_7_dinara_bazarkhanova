from django.db import models


# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (("new", "New"), ("in progress", "In Progress"), ("done", "Done"))

    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, verbose_name="Description")
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date and time")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date and time")
    price = models.DecimalField(verbose_name="Price")
    image = models.ImageField(verbose_name="Image", width_field=100, height_field=100)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, verbose_name="Description")

    def __str__(self):
        return f"{self.name}"

