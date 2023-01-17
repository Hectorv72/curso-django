from django.shortcuts import render

def herencia(request):
  return render(request=request, template_name='herencia.html', context={})

def ejemplo(request):
  return render(request=request, template_name='ejemplo.html', context={})