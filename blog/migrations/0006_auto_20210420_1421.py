# Generated by Django 3.0.8 on 2021-04-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210420_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='General', max_length=255),
        ),
    ]