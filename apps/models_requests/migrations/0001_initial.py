# Generated by Django 4.2.8 on 2023-12-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('languages', models.CharField(max_length=512, verbose_name='Языки')),
                ('town', models.CharField(max_length=128, verbose_name='Город')),
                ('website', models.CharField(max_length=256, verbose_name='Вебсайт')),
                ('about', models.TextField(verbose_name='Подробнее')),
            ],
            options={
                'verbose_name': 'Запрос моделя',
                'verbose_name_plural': 'Запросы моделям',
            },
        ),
    ]