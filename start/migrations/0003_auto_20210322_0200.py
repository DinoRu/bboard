# Generated by Django 3.1.7 on 2021-03-21 23:00

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20210322_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='image',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/static/start/img'), upload_to=''),
        ),
    ]
