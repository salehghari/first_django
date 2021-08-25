from django.contrib import admin
from .models import Article, Category

# admin.site.disable_action('delete_selected')

@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated >= 1:
        message_bit = "منتشر شد."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))

@admin.action(description='پیشنویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated >= 1:
        message_bit = "پیشنویش شد."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title','slug','parent','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','jpublish','status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug":("title",)}
    ordering = ["-status", "-publish"]
    actions = [make_published, make_draft]

admin.site.register(Article, ArticleAdmin)