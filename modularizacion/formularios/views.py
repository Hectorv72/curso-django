from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def form(request):
    return render(request=request, template_name='formularios/form.html', context={})


def goal(request):
    if request.method == "GET":
        name = request.GET['name']
        return render(request=request, template_name='formularios/success.html', context={'name': name})
    else:
        return HttpResponse('POST no es soportado en esta ruta')
