# Generated by Django 3.2.16 on 2022-12-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0016_paid_student_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_student',
            name='name',
            field=models.EmailField(default='kpa', max_length=150),
            preserve_default=False,
        ),
    ]
