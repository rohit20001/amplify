# Generated by Django 3.2.16 on 2022-12-24 08:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0022_paid_student_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_student',
            name='purchased_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]