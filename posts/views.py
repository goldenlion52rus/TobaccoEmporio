from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'posts/index.html')


def categories(request):
    return render(request, 'posts/index.html')


def archive(request, year):
    if year > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")
