# Generated by Django 3.2.16 on 2022-12-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0020_auto_20221224_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paid_student',
            name='course_name',
        ),
        migrations.AddField(
            model_name='paid_student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tmp.course'),
        ),
    ]
