from django.db import models

# Create your models here.


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.TextField(unique=True)


class Statistic(models.Model):
    date = models.TextField(),
    average_amount = models.FloatField()
    link_id = models.IntegerField()
