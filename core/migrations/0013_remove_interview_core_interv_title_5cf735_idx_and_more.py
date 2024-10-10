# Generated by Django 4.0 on 2024-10-10 11:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_aboutus_content_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='interview',
            name='core_interv_title_5cf735_idx',
        ),
        migrations.RemoveIndex(
            model_name='news',
            name='core_news_title_d9783a_idx',
        ),
        migrations.RemoveIndex(
            model_name='poetry',
            name='core_poetry_title_bf483c_idx',
        ),
        migrations.RemoveIndex(
            model_name='prose',
            name='core_prose_title_253236_idx',
        ),
        migrations.RemoveIndex(
            model_name='writings',
            name='core_writin_title_f081bc_idx',
        ),
        migrations.AddField(
            model_name='home',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AddField(
            model_name='interview',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AddField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AddField(
            model_name='poetry',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AddField(
            model_name='prose',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AddField(
            model_name='writings',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.get_image_upload_thumbnail),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='interview',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='poetry',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='prose',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='writings',
            name='image',
            field=models.ImageField(upload_to=core.models.get_image_upload_path),
        ),
    ]
