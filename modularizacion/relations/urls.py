from django.urls import path
from . import views

urlpatterns = [
    path("create/", view=views.create, name="create"),
    path("reporter/", view=views.reporter, name="reporter"),
    path("createmany/", view=views.createmany, name="createmany"),
    path("page/", view=views.page, name="page"),
]