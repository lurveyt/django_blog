#!/usr/env/bin python
"""
In general, an app that serves any sort of views
should contain its own urlconf. The project urlconf
should mainly include these where possible.

In order for our new urls to load, we’ll need to
include them in our project urlconf. Open urls.py
from the /mysite project package and add it.
"""

from django.urls import path
from blogging.views import stub_view, list_view, detail_view, LatestFeed, model_form, category_view

urlpatterns = [
    # path('', stub_view, name="blog_index"),
    path('', list_view, name="blog_index"),
    # path('post/<int:post_id>/', stub_view, name="blog_detail"),
    path('post/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feed/', LatestFeed(), name="latest_feed"),
    path('form/', model_form, name="model_form" ),
    # path('form/category/<int:cat_id>', category_view, name="category_view")
]