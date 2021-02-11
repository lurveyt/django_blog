from django.contrib import admin
from django.db.models import Count

from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
    # https://charlesleifer.com/blog/describing-relationships-djangos-manytomany-through/
    model = Category.posts.through
    insert_after = "title"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category.posts.through
    list_display = ("name", "description")
    exclude = ('posts',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category_count",
        "published_date",
    )
    inlines = [CategoryInline]

    # https://books.agiliq.com/projects/django-admin-cookbook/en/latest/optimize_queries.html
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _category_count=Count("categories", distinct=True),
        )
        return queryset

    def category_count(self, obj):
        return obj._category_count

# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
