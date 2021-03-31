# Generated by Django 3.1.7 on 2021-03-22 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0004_auto_20210322_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contacted', models.BooleanField(default=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='start.albums')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.contact')),
            ],
        ),
    ]