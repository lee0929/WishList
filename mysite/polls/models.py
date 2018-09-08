from django.db import models


class List(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    tax_flg = models.BooleanField(default=False)
    note = models.CharField(max_length=1000)
