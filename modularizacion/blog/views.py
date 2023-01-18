from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

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

    return render(request, 'blog/queries.html', {'authors': authors, 'author': author})
