from django.shortcuts import render
import markdown
from . import util
import random

def convert_to_HTML(entry_name):
    md = markdown.Markdown()
    entry = util.get_entry(entry_name)
    html = md.convert(entry) if entry else None
    return html

def index(request):
    return render(request, "encyclopedia/index.html", {
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
    entry_name2 = str(entry_name)
    html = convert_to_HTML(entry_name2)
    if html is None:
         return render(request, "encyclopedia/wrong_entry.html", {
             "entryTitle": entry_name
     })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entry_name
        })


def edit(request, entry_name):
    # entry_name2 = str(entry_name)
    # html = convert_to_HTML(entry_name2)
    content = util.get_entry(entry_name)
    return render(request, "encyclopedia/edit_entry.html", {
        "entry": content,
        "entryTitle": entry_name
    })
    


def save_edit(request):
    if request.method == 'POST':
        entry_title = request.POST['title']
        entry_text = request.POST['text']
        entries = util.list_entries()
        entries.remove(request.POST['title']) 
        util.save_entry(entry_title, entry_text)
        html = convert_to_HTML(entry_title)
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entry_title
        })


def rand(request):
    arr = util.list_entries()
    entry_title = random.choice(arr)
    html = convert_to_HTML(entry_title)
    return render(request, "encyclopedia/entry.html", {
        "entry": html,
        "entryTitle": entry_title
    })

        # previous feature: implement the edit entry function.
        # next feature: implement the search funtion.
