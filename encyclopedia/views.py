from django.shortcuts import render
import markdown
from . import util

def convert_to_HTML(entry_name):
    md = markdown.Markdown()
    entry = util.get_entry(entry_name)
    html = md.convert(entry) if entry else None
    return html

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

def save(request): 
    if request.method == 'POST':

        entry_title = request.POST['title']
        entry_text = request.POST['text']
        entries = util.list_entries()
        if entry_title in entries:
            return render(request, "encyclopedia/entry_exists.html", {
                "entryTitle": entry_title
            })
        else:
            util.save_entry(entry_title, entry_text)  
            html = convert_to_HTML(entry_title) 
            return render(request, "encyclopedia/entry.html", {          
                "entry": html,
                "entryTitle": entry_title
            })



def entry(request, entry_name):
    html = convert_to_HTML(entry_name)
    if html is None:
         return render(request, "encyclopedia/wrong_entry.html", {
             "entryTitle": entry_name
     })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entry_name
        })


        # next feature: implement the edit entry function.