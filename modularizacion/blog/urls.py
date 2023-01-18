from django.urls import path
from . import views

urlpatterns = [
    path("queries/", view=views.queries, name="queries"),
    path("update/", view=views.update, name="update"),
    path("restaurant/", view=views.restaurant, name="restaurant"),
]