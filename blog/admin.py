from django.contrib import admin

from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "content", "created_at", "is_published", "views_count",)
    list_filter = ("is_published",)
    search_fields = (
        "title",
        "content",
    )

# Register your models here.
