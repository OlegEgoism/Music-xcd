# Generated by Django 4.0 on 2021-12-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xcd', '0002_alter_samples_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='format',
            field=models.ManyToManyField(to='xcd.Format', verbose_name='Формат'),
        ),
    ]