# Generated by Django 4.2.16 on 2024-10-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliorat', '0009_bookreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookreview',
            old_name='user',
            new_name='reviewauthor',
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
