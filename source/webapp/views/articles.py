from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Article, StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices})
    article_data = {
        'name': request.POST.get('name'),
        'email': request.POST.get('email'),
        'text': request.POST.get('text')
    }
    Article.objects.create(**article_data)
    return redirect('index')


def update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.name = request.POST.get('name')
        article.email = request.POST.get('email')
        article.text = request.POST.get('text')
        return redirect('index')
    return redirect(request, 'article_update.html', context={'article': article, 'choices': StatusChoice.choices})


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'article': article})


def confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')
