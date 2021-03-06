# Generated by Django 3.0.7 on 2020-06-18 16:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Employee_ID')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(choices=[('p', 'Python'), ('j', 'Java'), ('js', 'Javascript'), ('DB', 'SQL'), ('a', 'REST_API')], max_length=2, verbose_name='Select_skill')),
                ('exp', models.IntegerField(verbose_name='Years of Experience')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('emp_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('emp_name', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Employee_Name')),
                ('DOJ', models.DateField(auto_now=True)),
                ('emp_photo', models.ImageField(upload_to='uploads/')),
                ('emp_unique', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employee')),
            ],
        ),
    ]
