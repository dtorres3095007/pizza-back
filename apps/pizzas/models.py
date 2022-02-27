from django.db import models
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'files/images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Pizza(models.Model):
    image = models.FileField(upload_to=path_and_rename, null=True)
    name = models.TextField()
    description  = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    state = models.CharField(choices=[("1", "Active"), ("0", "Inactive")], default="1", max_length=10)

    def __str__(self):
        return self.state

class Ingredient(models.Model):
    pizza = models.ForeignKey('pizzas.pizza', on_delete=models.PROTECT, related_name='pizza_ingredients')
    code = models.TextField()
    name  = models.TextField()
    price  = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    state = models.CharField(choices=[("1", "Active"), ("0", "Inactive")], default="1", max_length=10)

    def __str__(self):
        return self.state