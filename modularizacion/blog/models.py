from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.name


class Entry(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=5)
    def __str__(self):
        return  self.headline


class Place(models.Model):
    name = models.CharField(max_length=50)
    addres = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employes = models.IntegerField(default=1)

    def __str__(self):
        return self.place.name 

