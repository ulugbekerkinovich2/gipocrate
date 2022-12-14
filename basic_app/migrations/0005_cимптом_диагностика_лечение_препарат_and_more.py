# Generated by Django 4.0.6 on 2022-07-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_rename_mymodel_название_описание'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cимптом',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Диагностика',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Лечение',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Препарат',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Причин_возникновения',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
    ]
