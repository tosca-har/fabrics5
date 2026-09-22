from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect

def home(request):
    return render(request, "fabrics/home2.html")

def glossary(request):
    return render(request, "fabrics/glossary.html")

def lod(request):
    return render(request, "fabrics/lod.html")