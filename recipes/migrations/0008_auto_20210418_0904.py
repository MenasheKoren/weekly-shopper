# Generated by Django 3.0.5 on 2021-04-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20210418_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='static/img/%Y/%m/%d/'),
        ),
    ]
