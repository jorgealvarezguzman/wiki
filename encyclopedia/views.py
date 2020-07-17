from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util

import markdown2

from .forms import *

import random

# global variable
current_title = ""

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    global current_title
    current_title = title
    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

    return render(request, "encyclopedia/title.html",{
        "title": title,
        "entry": markdown2.markdown(entry)
    })


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            entries = util.list_entries()
            # case insensitive
            if search.lower() in [entry.lower() for entry in entries]:
                return redirect('title', search)
            else:
                # list of search substring in entry string
                search_entries = [entry for entry in entries if search.lower() in entry.lower()]
                if search_entries:
                    return render(request, "encyclopedia/search.html",{
                        "entries": search_entries
                    })
                return redirect('index')
        else:
            return redirect('index')


def newpage(request):
    return render(request, "encyclopedia/newpage.html")


def savenewpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            entries = util.list_entries()

            if title.lower() in [entry.lower() for entry in entries]:
                return render(request, "encyclopedia/error_newpage.html", {
                    "title": title
                })

            util.save_entry(title, content)

            return redirect('title', title)
    return redirect('index')


def editpage(request):
    global current_title
    entry = util.get_entry(current_title)
    return render(request, "encyclopedia/editpage.html",{
        "title": current_title,
        "entry": entry
    })


def saveeditpage(request):
    global current_title
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            editcontent = form.cleaned_data["editcontent"]

            util.save_entry(current_title, editcontent)
            return redirect('title', current_title)
    return redirect('index')


def randompage(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return redirect('title', random_title)
