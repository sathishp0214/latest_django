# Generated by Django 3.0.7 on 2020-06-30 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menus', to='django_app.Menu'),
        ),
    ]
