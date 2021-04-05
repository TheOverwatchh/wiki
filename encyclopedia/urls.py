from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entry, name="entry"),
    # path("wiki/CSS", views.cssPage, name="CSS"),
    # path("wiki/Django", views.djangoPage, name="Django"),
    # path("wiki/Git", views.gitPage, name="Git"),
    # path("wiki/HTML", views.htmlPage, name="HTML"),
    # path("wiki/Python", views.pythonPage, name="Python"),
    path("new", views.newEntry, name="new"),
    path("save", views.save, name="save")
]
