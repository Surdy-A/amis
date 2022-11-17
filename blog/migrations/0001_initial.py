# Generated by Django 4.1.1 on 2022-11-16 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='img')),
                ('slug', models.SlugField(default='', max_length=200)),
            ],
        ),
    ]
