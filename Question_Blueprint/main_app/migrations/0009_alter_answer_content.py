# Generated by Django 4.1.7 on 2023-07-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_question_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]