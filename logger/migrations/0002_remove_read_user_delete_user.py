# Generated by Django 4.0.1 on 2022-01-24 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
