# Generated by Django 3.0.5 on 2021-04-18 09:53

from django.db import migrations
import djfractions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20210418_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='quantity_fraction',
            field=djfractions.models.fields.DecimalFractionField(coerce_thirds=True, decimal_places=4, default=0, help_text='Optional fraction', limit_denominator=None, max_digits=4, verbose_name='Fraction'),
        ),
    ]