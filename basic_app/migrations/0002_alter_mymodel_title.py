# Generated by Django 4.0.6 on 2022-07-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='title',
            field=models.TextField(verbose_name='название'),
        ),
    ]
