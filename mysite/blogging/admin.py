from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
    # https://charlesleifer.com/blog/describing-relationships-djangos-manytomany-through/
    model = Category.posts.through
    insert_after = "title"

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
