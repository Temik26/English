from django.urls import path
from .views import (WordsListView, TopicsListView,
                    TopicWordsListView, DetailWordView)

urlpatterns = [
    path('all_words/', WordsListView.as_view()),
    path('all_topics/', TopicsListView.as_view()),
    path('topic_words/<topic_id>/', TopicWordsListView.as_view()),
    path('word_details/', DetailWordView.as_view())
]
