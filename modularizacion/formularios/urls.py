from django.urls import path
from . import views

urlpatterns = [
    path("form/", view=views.form, name="form"),
    path("goal/", view=views.goal, name="goal"),
    path("comment/", view=views.comment, name="comment"),
    path("widget/", view=views.widget, name="widget"),
    path("index/", view=views.index, name="index"),
]
