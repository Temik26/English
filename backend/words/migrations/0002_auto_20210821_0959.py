# Generated by Django 3.2.6 on 2021-08-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='word_example',
            field=models.TextField(default='No example', max_length=255, verbose_name='Example'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Example',
        ),
    ]
