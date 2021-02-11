from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
    # https://charlesleifer.com/blog/describing-relationships-djangos-manytomany-through/
    model = Category.posts.through
    insert_after = "title"

class CategoryAdmin(admin.ModelAdmin):
    model = Category.posts.through
    list_display = ("name", "description")
    exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("title", "author", "modified_date", "published_date")
    inlines = [CategoryInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
