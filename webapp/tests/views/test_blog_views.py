from django import urls
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from webapp.tests.factories.blog_factories import PostFactory
from webapp.views.blog_views import PostViewset

class PostViewsetTest(APITestCase):

  def setUp(self):
    self.url = urls.reverse('posts-list')
    self.client = APIClient()

  def test_url_exist(self):
    self.assertEqual(self.url, '/api/posts/')

  def test_view_returns_200(self):
    
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_view_returns_list_posts(self):
  
    PostFactory()
    PostFactory()

    response = self.client.get(self.url)

    self.assertEqual(len(response.data['posts']), 2)

  def test_view_retrieve_returns_200(self):

    post = PostFactory()

    response = self.client.get("{}{}/".format(self.url, post.id))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_view_retrieve_returns_404_if_object_doesnt_exits(self):
  
    response = self.client.get("{}{}/".format(self.url, 0))

    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_view_retrieve_returns_data(self):
  
    post = PostFactory()

    response = self.client.get("{}{}/".format(self.url, post.id))

    self.assertEqual(response.data['id'], post.id)

  def test_latest_post_returns_latest_post(self):

    post1 = PostFactory(date_posted=datetime.now() - timedelta(days=1))
    post2 = PostFactory(date_posted=datetime.now())

    self.assertEqual(post2.id, PostViewset._get_latest_post().id)