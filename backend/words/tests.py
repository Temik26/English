from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Topic, Unit, Dictionary


class WordsTest(APITestCase):
    def setUp(self):
        unit = Unit.objects.create(unit='Metaphorical')
        first_topic = Topic.objects.create(topic_name='Social',
                                           link_to_photo='photos.ru/social_logo')
        second_topic = Topic.objects.create(topic_name='Medicine',
                                            link_to_photo='photos.ru/medicine_logo')
        Dictionary.objects.create(word='Trade', transcription='treɪd',
                                  topic_id=first_topic, unit_id=unit)
        Dictionary.objects.create(word='Transplant', transcription='ˈtrænsplænt',
                                  topic_id=second_topic, unit_id=unit)

    def test_get_words(self):
        response = self.client.get(reverse('all_words'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue({'id': 3, 'word': 'Trade'} in response.json())

    def test_get_topics(self):
        response = self.client.get(reverse('all_topics'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue({'id': 1, 'topic_name': 'Social',
                         'link_to_photo': 'http://testserver/images/photos.ru/social_logo'} in response.json())
