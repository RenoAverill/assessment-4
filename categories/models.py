from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Category Name: {self.name}"


class Post(models.Model):
    item = models.TextField()
    detail = models.TextField()
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"Item: {self.item}, Detail: {self.detail}"
