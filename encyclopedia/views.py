from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def cssPage(request):
    return render(request, "encyclopedia/CSS.html", {
        "entries": util.list_entries()
    })    

def htmlPage(request):
    return render(request, "encyclopedia/HTML.html", {
        "entries": util.list_entries()
    })

def djangoPage(request):
    return render(request, "encyclopedia/Django.html", {
        "entries": util.list_entries()
    })


def gitPage(request):
    return render(request, "encyclopedia/Git.html", {
        "entries": util.list_entries()
    })


def pythonPage(request):
    return render(request, "encyclopedia/Python.html", {
        "entries": util.list_entries()
    })

def newEntry(request): 
    return render(request, "encyclopedia/new-entry.html", {
        "entries": util.list_entries()
    })


