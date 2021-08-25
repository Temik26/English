from rest_framework import serializers
from .models import Dictionary, Topic, Translation


class DictionaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'word')


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicWordsSerializer(serializers.ModelSerializer):
    translation_type = serializers.StringRelatedField()
    word = serializers.StringRelatedField()

    class Meta:
        model = Translation
        fields = ('id', 'translation_type', 'word')


class WordSerializer(serializers.ModelSerializer):
    translation_type = serializers.StringRelatedField()

    class Meta:
        model = Translation
        fields = ('id', 'translation_type', 'translation', 'word_example')


class DetailWordInfoSerializer(serializers.ModelSerializer):
    meanings = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Dictionary
        fields = ('word', 'transcription', 'meanings')
