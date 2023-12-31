# Generated by Django 5.0 on 2023-12-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'сообщения',
                'ordering': ('name',),
            },
        ),
    ]
