from rest_framework import generics
from .models import Dictionary, Topic, Translation
from .serializers import (DictionaryListSerializer, TopicListSerializer,
                          TopicWordsSerializer, DetailWordInfoSerializer)
from rest_framework import filters


class WordsListView(generics.ListAPIView):
    """Get all words and search words by a letter"""
    serializer_class = DictionaryListSerializer
    queryset = Dictionary.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^word']


class TopicsListView(generics.ListAPIView):
    """Get all topics with a link to the photo"""
    serializer_class = TopicListSerializer
    queryset = Topic.objects.all()


class TopicWordsListView(generics.ListAPIView):
    """Show all words filtered by a topic"""
    serializer_class = TopicWordsSerializer

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Translation.objects.filter(word__topic_id_id=topic_id).select_related('word')


class DetailWordView(generics.ListAPIView):
    """Show all information related to a word"""
    serializer_class = DetailWordInfoSerializer
    queryset = Dictionary.objects.all()
