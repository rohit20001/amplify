# Generated by Django 3.2.16 on 2022-12-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0019_auto_20221222_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_student',
            name='course_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='paid_student',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
