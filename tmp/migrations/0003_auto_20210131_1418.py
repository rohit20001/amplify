# Generated by Django 3.1.4 on 2021-01-31 08:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0002_auto_20210131_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='aboutAuthor',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='postedBy',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='postedBy_project',
            field=models.CharField(max_length=50),
        ),
    ]