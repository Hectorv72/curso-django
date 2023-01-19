from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

# Create your views here.


def form(request):
    return render(request=request, template_name='formularios/form.html', context={})


def comment(request):
    comment_form = CommentForm({'name': 'Hector'})
    return render(request=request, template_name='formularios/comment.html', context={'comment_form': comment_form})


def widget(request):
    contact_form = ContactForm()
    return render(request=request, template_name='formularios/widget.html', context={'contact_form': contact_form})


def goal(request):
    if request.method == "GET":
        name = request.GET['name']
        return render(request=request, template_name='formularios/success.html', context={'name': name})
    else:
        return HttpResponse('POST no es soportado en esta ruta')
