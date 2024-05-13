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


class RespuestasForm(models.Model):

    mail = models.EmailField()
    timestamp = models.DateTimeField()
    genero = models.CharField(max_length=10)
    jerarquia = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()
    r6 = models.IntegerField()
    r7 = models.IntegerField()
    r8 = models.IntegerField()
    r9 = models.IntegerField()
    r10 = models.IntegerField()
    r11 = models.IntegerField()
    r12 = models.IntegerField()
    r13 = models.IntegerField()
    r14 = models.IntegerField()
    r15 = models.IntegerField()

