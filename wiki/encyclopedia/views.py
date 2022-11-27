from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "info" : util.get_entry(title),
    } )

def search(request):
    q = request.GET['q']
    entries = util.list_entries()
    for entry in entries:
        if q in entry:
            return redirect("entry", title=q)
    
    return render(request, "encyclopedia/search.html")


