from django.urls import path
from .views import (WordsListView, TopicsListView,
                    TopicWordsListView, DetailWordView)

urlpatterns = [
    path('all_words/', WordsListView.as_view(), name='all_words'),
    path('all_topics/', TopicsListView.as_view(), name='all_topics'),
    path('topic_words/<topic_id>/', TopicWordsListView.as_view(), name='topic_words'),
    path('word_details/', DetailWordView.as_view(), name='words_details')
]
