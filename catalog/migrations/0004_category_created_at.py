# Generated by Django 5.0 on 2023-12-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=0, verbose_name='Создание'),
            preserve_default=False,
        ),
    ]
