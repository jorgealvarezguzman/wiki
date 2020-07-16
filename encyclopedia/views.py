from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

    return render(request, "encyclopedia/title.html",{
        "title": title,
        "entry": markdown2.markdown(entry)
    })
