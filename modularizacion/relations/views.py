from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
  return HttpResponse('funciona')


def manytoone(request):
  return HttpResponse('funciona')