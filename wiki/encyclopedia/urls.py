from django.urls import path
import re
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:page>", views.markdown2css, name="markdown2css"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("random/", views.random, name="random"),
    path("pagetoedit/", views.pagetoedit, name="pagetoedit"),
    path("editpage/", views.editpage, name="editpage")
]
