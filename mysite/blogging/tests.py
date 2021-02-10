from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import utc
import datetime

from blogging.models import Post, Category

import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s "
                           "%(levelname)s "
                           "%(filename)s.%(funcName)s():%(lineno)d "
                           "> %(message)s")
logger = logging.getLogger(__name__)

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self) -> None:
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


# and the test case and test
class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')
        # the content of the rendered response is always a byte string
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """
        title = models.CharField(max_length=150)
        text = models.TextField(blank=True)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_date = models.DateTimeField(auto_now_add=True)
        modified_date = models.DateTimeField(auto_now=True)
        published_date = models.DateTimeField(blank=True, null=True)
        """
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            # logger.info(f"post{count} created")
            # logger.info(f"post.title, {post.title}")
            # logger.info(f"post.text, {post.text}")
            # logger.info(f"post.author, {post.author}")
            # logger.info(f"post.created_date, {post.created_date}")
            # logger.info(f"post.modified_date, {post.modified_date}")
            # logger.info(f"post.published_date, {post.published_date}")
            resp = self.client.get('/post/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
