# Generated by Django 3.2.3 on 2022-12-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0025_alter_certi_certi_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certi',
            name='certi_id',
            field=models.CharField(max_length=20),
        ),
    ]