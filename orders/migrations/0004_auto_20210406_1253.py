# Generated by Django 3.1.5 on 2021-04-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210314_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedorder',
            name='ordered_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Sifarişin edilmə tarixi'),
        ),
    ]
