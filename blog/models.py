from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name = "عنوان دسته‌بندي")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس دسته‌بندي")
    status = models.BooleanField(default=True, verbose_name= "آيا نمايش داده شود؟")
    position = models.IntegerField(verbose_name="پوزيشن")

    class Meta:
        verbose_name = "دسته‌بندي"
        verbose_name_plural = "دسته‌بندي ها"
        ordering = ["position"]

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES =(
        ('d', 'پيشن‌‌ويس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name = "عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name= "دسته‌بندي")
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