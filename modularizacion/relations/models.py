from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

class Article(models.Model):
    headline = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Page(models.Model):
    headline = models.CharField(max_length=50)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
