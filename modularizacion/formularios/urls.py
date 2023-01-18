from django.urls import path
from . import views

urlpatterns = [
    path("form/", view=views.form, name="form"),
    path("goal/", view=views.goal, name="goal"),
]
