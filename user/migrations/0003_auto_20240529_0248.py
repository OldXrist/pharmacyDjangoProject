# Generated by Django 3.1.14 on 2024-05-28 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20240529_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='gender',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
