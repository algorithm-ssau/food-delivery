from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    categoryId = models.IntegerField()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"

    def __str__(self):
        return self.title
