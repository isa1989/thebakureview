# Generated by Django 4.0 on 2024-10-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_interview_slug_news_slug_poetry_slug_prose_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='submissionguidelines',
            name='content',
            field=models.TextField(),
        ),
    ]
