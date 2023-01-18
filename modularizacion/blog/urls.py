from django.urls import path
from . import views

urlpatterns = [
    path("queries/", view=views.queries, name="queries")
]