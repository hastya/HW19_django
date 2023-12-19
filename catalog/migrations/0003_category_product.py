# Generated by Django 5.0 on 2023-12-19 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_feedback_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Категория')),
                ('category_descr', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'категории',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='наименование')),
                ('product_descr', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение(превью)')),
                ('product_price_each', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='цена за штуку')),
                ('product_date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('product_date_last', models.DateTimeField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукты',
                'ordering': ('product_name',),
            },
        ),
    ]