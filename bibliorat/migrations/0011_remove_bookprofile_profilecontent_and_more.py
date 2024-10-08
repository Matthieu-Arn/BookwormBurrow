# Generated by Django 4.2.16 on 2024-10-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliorat', '0010_rename_user_bookreview_reviewauthor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookprofile',
            name='profilecontent',
        ),
        migrations.AddField(
            model_name='bookprofile',
            name='profileanalysis',
            field=models.TextField(default='Analysis goes here'),
        ),
        migrations.AddField(
            model_name='bookprofile',
            name='profilesynopsis',
            field=models.TextField(default='Synopsis goes here'),
        ),
        migrations.AlterField(
            model_name='bookprofile',
            name='authorname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_authors', to='bibliorat.bookauthor'),
        ),
    ]
