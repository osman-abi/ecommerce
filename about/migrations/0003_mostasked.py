# Generated by Django 3.1.5 on 2021-03-15 09:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_project_projectimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostAsked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='sual')),
                ('content', ckeditor.fields.RichTextField(verbose_name='cavab')),
            ],
        ),
    ]
