# Generated by Django 3.2.16 on 2022-12-22 18:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0018_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_by',
            field=models.CharField(default='kps', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='brief_content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
