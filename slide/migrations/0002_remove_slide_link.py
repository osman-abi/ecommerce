# Generated by Django 3.1.5 on 2021-03-14 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='link',
        ),
    ]
