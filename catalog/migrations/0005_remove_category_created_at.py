# Generated by Django 5.0 on 2023-12-19 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
