from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from bookapp.models import Book

# Create your views here.

def archive(request):
    posts = Book.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))