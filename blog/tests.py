import datetime

from django.test import TestCase
from blog.models import Post


class PostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='Title',
            description='Description',
            created_date=datetime.datetime.now(),
            published=True
        )

    def test_post_field_names(self):
        post = Post.objects.get(title='Title')
        title = post._meta.get_field('title').verbose_name
        description = post._meta.get_field('description').verbose_name
        created_date = post._meta.get_field('created_date').verbose_name
        published = post._meta.get_field('published').verbose_name
        self.assertEqual(title, 'title')
        self.assertEqual(description, 'description')
        self.assertEqual(created_date, 'created date')
        self.assertEqual(published, 'published')
