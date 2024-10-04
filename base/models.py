from django.db import models

# Create your models here.
#Item model with name, created (time) fields

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
