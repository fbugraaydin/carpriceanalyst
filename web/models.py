from django.db import models


class Link(models.Model):
    link = models.TextField(unique=True)


class Statistic(models.Model):
    date = models.DateField()
    average_amount = models.FloatField()
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
