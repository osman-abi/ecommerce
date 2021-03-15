# Generated by Django 3.1.5 on 2021-03-05 12:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Başlıq')),
                ('duration', models.CharField(max_length=250, verbose_name='Zaman aralığı')),
                ('small_text', ckeditor.fields.RichTextField(max_length=300, verbose_name='Qısa mətn')),
                ('content', ckeditor.fields.RichTextField(max_length=5000, verbose_name='Ətraflı mətn')),
            ],
            options={
                'verbose_name': 'Kampaniya',
                'verbose_name_plural': 'Kampaniyalar',
            },
        ),
    ]
