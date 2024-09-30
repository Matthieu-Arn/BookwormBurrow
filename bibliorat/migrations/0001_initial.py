# Generated by Django 4.2.16 on 2024-09-30 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktitle', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('profilecontent', models.TextField()),
                ('bookgenre', models.CharField(max_length=200, unique=True)),
                ('publicationyear', models.CharField(max_length=200, unique=True)),
                ('originallanguage', models.CharField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('profileauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]