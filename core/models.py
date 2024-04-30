from django.db import models

# Create your models here.

class Altmetrics(models.Model):

    doi = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    mendeley_readers = models.IntegerField()
    score = models.IntegerField()
    facebook = models.IntegerField()
    x = models.IntegerField()
    blogs = models.IntegerField()
    news = models.IntegerField()
    reddit = models.IntegerField()
    stackoverflow = models.IntegerField()
    policies = models.IntegerField()
    patents = models.IntegerField()
    youtube = models.IntegerField()
    wikipedia = models.IntegerField()
    year = models.IntegerField()
    total = models.IntegerField()
