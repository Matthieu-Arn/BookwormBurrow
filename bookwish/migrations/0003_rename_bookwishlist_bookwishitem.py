# Generated by Django 4.2.16 on 2024-10-04 00:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliorat', '0012_alter_bookauthor_options_alter_bookprofile_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookwish', '0002_bookwishlist_personalnotes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookwishlist',
            new_name='Bookwishitem',
        ),
    ]