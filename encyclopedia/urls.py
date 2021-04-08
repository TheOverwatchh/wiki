from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entry, name="entry"),
    path("wiki/<str:entry_name>/edit", views.edit, name="edit_entry"),
    path("random", views.rand, name="rand"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("new", views.newEntry, name="new"),
    path("save", views.save, name="save")
]
