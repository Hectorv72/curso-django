from django.http import HttpResponse
from django.shortcuts import render

# def saludo(request):
#   return HttpResponse('Hola mundo')

# def despedida(request):
#   return HttpResponse('Adios mundos')

# def adulto(request, edad):
#   if(edad >= 18):
#     return HttpResponse('Es mayor de edad')
#   else:
#     return HttpResponse('No es mayor de edad')
  
def simple(request):
  return render(request=request, template_name='simple.html', context={})

def dinamico(request, name):
  categories = ['code','design','marketing', 'business']
  context = {'name': name, 'categories': categories}
  return render(request=request, template_name='dinamico.html', context=context)

def estaticos(request):
  return render(request=request, template_name='estaticos.html', context={})