from django.urls import path
from . import views

urlpatterns = [
    path("create/", view=views.create, name="create"),
    path("manytoone/", view=views.manytoone, name="manytoone"),
]