# Generated by Django 3.1.5 on 2021-03-29 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210329_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='products.Category', verbose_name='Məhsulun kateqoriyası'),
        ),
    ]
