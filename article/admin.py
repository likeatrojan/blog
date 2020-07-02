from django.contrib import admin

from .models import Article
from .models import Comment

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author"]
    list_display_links = ["author"]
    search_fields = ["title","content"]
    list_filter = ["created_date"]
    class Meta:
        model = Article