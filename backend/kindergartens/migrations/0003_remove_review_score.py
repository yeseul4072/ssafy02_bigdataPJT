# Generated by Django 3.1.1 on 2020-10-05 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kindergartens', '0002_remove_review_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='score',
        ),
    ]
