from django.urls import path
from . import views

urlpatterns = [
    path('test/', view=views.test, name='test'),
    path('create/', view=views.create, name='create'),
    path('delete/', view=views.delete, name='delete')
]