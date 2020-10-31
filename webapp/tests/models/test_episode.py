from unittest import TestCase

from webapp.models.episode import Episode
from webapp.tests.factories.episode_factories import EpisodeFactory
from webapp.tests.factories.character_factories import CharacterFactory

class EpisodeTest(TestCase):

  def test_filters_characters_properly(self):
    char1 = CharacterFactory()
    char2 = CharacterFactory()
    
    ep1 = EpisodeFactory().characters.set([char1])
    ep2 = EpisodeFactory().characters.set([char1])
    ep3 = EpisodeFactory().characters.set([char2])

    self.assertEqual(2, len(Episode.objects.filter_episodes(characters=[char1.name])))

  def test_filters_seasons_properly(self):

    ep1 = EpisodeFactory(season=1)
    ep2 = EpisodeFactory(season=2)
    ep3 = EpisodeFactory(season=2)

    self.assertEqual(2, len(Episode.objects.filter_episodes(seasons=[2])))

  def test_filters_highest_rated_episodes_properly(self):

    ep1 = EpisodeFactory(rating=9)
    ep2 = EpisodeFactory(rating=9.6)
    ep3 = EpisodeFactory(rating=6)

    self.assertEqual(2, len(Episode.objects.filter_episodes(is_classic=True)))
