# Generated by Django 3.1.5 on 2021-03-05 12:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/blog/', verbose_name='Şəkil')),
                ('title', models.CharField(max_length=300, verbose_name='Başlıq')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=5000, verbose_name='Mətn')),
            ],
            options={
                'verbose_name': 'Məqalə',
                'verbose_name_plural': 'Məqalələr',
            },
        ),
    ]