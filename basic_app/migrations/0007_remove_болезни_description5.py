# Generated by Django 4.0.6 on 2022-07-28 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_болезни_delete_cимптом_delete_диагностика_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='болезни',
            name='description5',
        ),
    ]
