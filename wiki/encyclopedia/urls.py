from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.markdown2html, name="CSS"),
]
