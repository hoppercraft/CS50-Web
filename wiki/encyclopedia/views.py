from django.shortcuts import render
from . import util
import markdown2
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def markdown2css(request, page):
    try:
        return render(request, "encyclopedia/markdown.html",{"page":markdown2.markdown(util.get_entry(page)),"title":page})
    except:
        return render(request, "encyclopedia/error.html", {
            "message": "Page Not Found"
        })
    
def search(request):
    if request.method=="POST":
        entry_search = request.POST['q']
        try:
            page = markdown2.markdown(util.get_entry(entry_search))
            return render(request, "encyclopedia/markdown.html",{
                "page":page,
                "title":entry_search
                })
        except:
            check = util.list_entries()
            recommendation=[]
            for entry in check:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommendation":recommendation
            })
        
def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        markdown = request.POST['markdown']
        titles = util.list_entries()
        if title in titles:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, markdown)
        return render(request, "encyclopedia/markdown.html", {
            "page":markdown2.markdown(util.get_entry(title)),
            "title":title
        })
    
def random(request):
    titles = util.list_entries()
    title = choice(titles)
    return render(request, "encyclopedia/markdown.html", {
        "page":markdown2.markdown(util.get_entry(title)),
        "title":title
    })

def pagetoedit(request):
    return render(request, "encyclopedia/pagetoedit.html")
    
def editpage(request):
        if request.method == "GET":
            title=request.GET['title']
            titles = util.list_entries()
            if title in titles:
                return render(request, "encyclopedia/editpage.html", {
                    "title":title,
                    "before":util.get_entry(title)
                })
            else:
                 return render(request, "encyclopedia/error.html",{
                      "message": "Entry page not found"
                 })
        else:
            title = request.POST['title']
            markdown = request.POST['markdown']
            util.save_entry(title, markdown)
        return render(request, "encyclopedia/markdown.html", {
            "page":markdown2.markdown(util.get_entry(title)),
            "title":title
            })
        
