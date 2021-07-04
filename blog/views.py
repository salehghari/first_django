from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse
from .models import Article, Category

def home(request):
    context = {
        "articles" : Article.objects.filter(status='p'),
        "category" : Category.objects.filter(status=True)
    }
    return render(request,"blog/home.html", context)

def detail(request, slug):
    context = {
        "article" : get_object_or_404(Article, slug=slug, status="p"),
        "category" : Category.objects.filter(status=True)
    }
    return render(request,"blog/detail.html", context)
