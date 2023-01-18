from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Restaurant, Place

# Create your views here.
def queries(request):
    # todo
    authors = Author.objects.all()
    # especifico
    author = Author.objects.get(id=2)
    # limitado (10)
    authors = Author.objects.all()[:10]

    # salteado (offset) (5,10)
    authors = Author.objects.all()[5:15]

    # ordenados
    authors = Author.objects.all().order_by('email')

    # por menor y mayor
    # __lte: menor o igual
    # __gte: mayor o igual
    # __lt: menor que
    # __gt: menor que
    # __contains: contiene
    # __exact: contiene

    # contiene texto
    filtered = Author.objects.filter(name__contains='result')

    return render(request, 'blog/queries.html', {'authors': authors, 'author': author, 'filtered': filtered})


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Hector"
    author.email = "Hector@gmail.com"
    author.save()
    return HttpResponse('Author modificado')

def restaurant(request):
    place = Place(name="Villa do carlo", addres="Brasil 12300")
    place.save()

    restaurant = Restaurant(place=place, number_of_employes=5)
    restaurant.save()
    return HttpResponse(restaurant.place.name)