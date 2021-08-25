from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_converter


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class Category(models.Model):
    parent = models.ForeignKey("self", default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name="زیر‌دسته")
    title = models.CharField(max_length=200, verbose_name = "عنوان دسته‌بندي")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس دسته‌بندي")
    status = models.BooleanField(default=True, verbose_name= "آيا نمايش داده شود؟")
    position = models.IntegerField(verbose_name="پوزيشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندي ها"
        ordering = ["parent__id", "position"]

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES =(
        ('d', 'پيشن‌‌ويس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name = "عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name= "دسته‌بندي", related_name="articles")
    description = models.TextField(verbose_name = "محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name = "تصوير مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name = "وضعيت")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img width=100 height=60 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"

    objects = ArticleManager()