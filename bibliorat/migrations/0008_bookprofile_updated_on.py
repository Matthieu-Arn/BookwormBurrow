# Generated by Django 4.2.16 on 2024-09-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliorat', '0007_bookprofile_authorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookprofile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
