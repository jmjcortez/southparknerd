from django import urls
from datetime import datetime, timedelta
from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class EpisodeViewsetTest(APITestCase):

  def setUp(self):
    self.url = urls.reverse('episodes-list')
    self.client = APIClient()

  def test_url_exist(self):
    self.assertEqual(self.url, '/api/episodes/')

  def test_view_returns_200(self):
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  @patch('webapp.views.episode_views.Episode')
  def test_random_view_returns_200_and_calls_filter(self, ep_objects):
    response = self.client.get('{}random/'.format(self.url))

    ep_objects.objects.filter_episodes.assert_called_with(characters=[], seasons=[], is_classic=False);

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  @patch('webapp.views.episode_views.Episode')
  def test_random_view_returns_200_calls_filter_with_characters(self, ep_objects):

    query = 'characters=Kenny&characters=Kyle'

    response = self.client.get('{}random/?{}'.format(self.url, query))

    ep_objects.objects.filter_episodes.assert_called_with(characters=['Kenny', 'Kyle'], seasons=[], is_classic=False);

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  @patch('webapp.views.episode_views.Episode')
  def test_random_view_returns_200_calls_filter_with_seasons(self, ep_objects):

    query = 'seasons=69&seasons=67'

    response = self.client.get('{}random/?{}'.format(self.url, query))

    ep_objects.objects.filter_episodes.assert_called_with(characters=[], seasons=[69,67], is_classic=False);

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  @patch('webapp.views.episode_views.Episode')
  def test_random_view_returns_200_calls_filter_with_characters(self, ep_objects):

    query = 'is_classic=1'

    response = self.client.get('{}random/?{}'.format(self.url, query))

    ep_objects.objects.filter_episodes.assert_called_with(characters=[], seasons=[], is_classic=True);

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  @patch('webapp.views.episode_views.Episode')
  def test_random_view_returns_200_calls_all_filters(self, ep_objects):

    query = 'characters=Kenny&characters=Kyle&seasons=69&seasons=67&is_classic=1'

    response = self.client.get('{}random/?{}'.format(self.url, query))

    ep_objects.objects.filter_episodes.assert_called_with(characters=['Kenny','Kyle'], seasons=[69,67], is_classic=True);

    self.assertEqual(response.status_code, status.HTTP_200_OK)
