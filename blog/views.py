from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category

def home(request):
    articles = Article.objects.filter(status='p').order_by('publish')
    context = {"articles" : articles}
    return render(request,"blog/home.html", context)

def detail(request, slug):
    context = {"article" : get_object_or_404(Article, slug=slug, status="p")}
    return render(request,"blog/detail.html", context)
