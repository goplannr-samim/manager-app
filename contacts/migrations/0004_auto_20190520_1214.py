# Generated by Django 2.1.7 on 2019-05-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_merge_20190214_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Last name'),
        ),
    ]
