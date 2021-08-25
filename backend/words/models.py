from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=50,
                                  verbose_name='Topic name')
    link_to_photo = models.ImageField(verbose_name='Topic photo')

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.topic_name


class Unit(models.Model):
    unit = models.CharField(max_length=50,
                            verbose_name='Unit')

    class Meta:
        verbose_name_plural = 'Units'

    def __str__(self):
        return self.unit


class Dictionary(models.Model):
    word = models.CharField(max_length=50,
                            verbose_name='Word',
                            unique=True)
    transcription = models.CharField(max_length=50,
                                     verbose_name='Transcription')
    topic_id = models.ForeignKey(Topic,
                                 verbose_name='Topic',
                                 on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit,
                                verbose_name='Unit',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Dictionary'

    def __str__(self):
        return self.word


class TranslationType(models.Model):
    translation_type = models.CharField(max_length=50,
                                        verbose_name='Translation type',
                                        unique=True)

    class Meta:
        verbose_name = 'Translation type'
        verbose_name_plural = 'Translation types'

    def __str__(self):
        return self.translation_type


class Translation(models.Model):
    word = models.ForeignKey(Dictionary,
                             verbose_name='Word',
                             on_delete=models.CASCADE,
                             related_name='meanings')
    translation = models.CharField(max_length=50,
                                   verbose_name='Translation')
    translation_type = models.ForeignKey(TranslationType,
                                         verbose_name='Translation type',
                                         on_delete=models.CASCADE)
    word_example = models.TextField(max_length=255,
                                    verbose_name='Example')

    class Meta:
        verbose_name_plural = 'Translation'

    def __str__(self):
        return self.translation
