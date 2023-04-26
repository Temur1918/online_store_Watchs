# Generated by Django 4.1 on 2023-04-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0014_watchmodel_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchmodel',
            name='about_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='about_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='about_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='subtitle_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='subtitle_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='subtitle_uz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='title_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='title_uz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
