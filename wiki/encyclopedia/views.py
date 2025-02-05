from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def markdown2html(CSS):
    file = util.get_entry(request)
    mark = markdown.Markdown()
    if request == None:
        return None
    return mark.convert(request)
