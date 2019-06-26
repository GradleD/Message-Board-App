from django.test import TestCase
from django.urls import reverse

from .models import  Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post =Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')

class HomepageViewTest(TestCase):
    def setUp(self) :
        Post.objects.create(text='Another test')

    def test_view_url_exist_at_proper_location(self):
         resp = self.client.get('/')
         self.assertEqual(resp.status_code, 200)

    def test_view_utl_by_name(self):
          resp =self.client.get(reverse('home'))
          self.assertEqual(resp.status_code,200)

    def test_view_user_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'home.html')