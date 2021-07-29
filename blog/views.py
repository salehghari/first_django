from django.db import models
from django.views.generic import ListView, DetailView
from django.core.paginator import Page, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse
from .models import Article, Category
class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3

# def detail(request, slug):
#     context = {
#         "article" : get_object_or_404(Article.objects.published(), slug=slug),
#     }
#     return render(request,"blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)

def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 2)
    articles = paginator.get_page(page)
    context = {
        "category" : category,
        "articles" : articles,
    }
    return render(request,"blog/category.html", context)