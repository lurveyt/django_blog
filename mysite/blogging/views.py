from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post, Category

# https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/#a-simple-example
from django.contrib.syndication.views import Feed
from django.urls import reverse


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join([f"\t{a}" for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join([f"\t{k}:{v}" for k,v in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    # find only published
    published = Post.objects.exclude(published_date__exact=None)
    # sort reverse
    posts = published.order_by('-published_date')
    # push to page context
    context = {'posts': posts}
    #
    #   VERBOSE WAY
    #
    # template = loader.get_template('blogging/list.html')
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")

    """This is a common pattern in Django views:
    get a template from the loader
    build a context
    render the template
    return an HttpResponse
    So common in fact that Django provides a shortcut for us to use:

    render(request, template[, ctx][, ctx_instance])"""
    #
    #   Django shortcut way
    #
    return render(request, "blogging/list.html", context)


def detail_view(request, post_id):
    # find only published
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post':post}
    return render(request=request,
                  template_name='blogging/detail.html',
                  context=context)


class LatestFeed(Feed):
    title = "Stuf I made"
    link = "/feed/"
    description = "The latest stuff from me!"

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        # sort reverse
        return published.order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return f"Written by: {item.author.username} " \
               f"on {item.published_date}"

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
