# Generated by Django 3.0.7 on 2020-06-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_auto_20200629_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=25),
        ),
    ]
