from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label="search")

class NewPageForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")

class EditPageForm(forms.Form):
    editcontent = forms.CharField(label="editcontent")
