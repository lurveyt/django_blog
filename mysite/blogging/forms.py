#!/usr/env/bin python
from django.forms import ModelForm, inlineformset_factory
from blogging.models import Post, Category

class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "author",
            ]

# PostInlineFormSet = inlineformset_factory(Category, Post,
#                                           fields=(
#                                               "title",
#                                               "text",
#                                               "author",
#                                               "categories",
#                                           ))