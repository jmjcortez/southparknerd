from django import urls
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class PostViewsetTest(APITestCase):

  def setUp(self):
    self.url = urls.reverse('characters-list')
    self.client = APIClient()

  def test_url_exist(self):
    self.assertEqual(self.url, '/api/characters/')

  def test_view_returns_200(self):      
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
