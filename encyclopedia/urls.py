from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("savenewpage", views.savenewpage, name="savenewpage"),
    path("editpage", views.editpage, name="editpage"),
    path("saveeditpage", views.saveeditpage, name="saveeditpage"),
    path("randompage", views.randompage, name="randompage")
]
