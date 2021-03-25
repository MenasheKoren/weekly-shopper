from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.DecimalField(max_value=999, min_value=0.01, decimal_places=2)
    
    OUNCES = 'OZ'
    POUND = 'LB'
    MILLIGRAM = 'MG'
    GRAM = 'GR'
    KILOGRAM = 'KG'

    TEASPOON = 'TSP'
    TABLESPOON = 'TBSP'
    FLUID_OUNCE = 'FL_OZ'
    CUP = 'CUP'
    PINT = 'PT'
    QUART = 'QT'
    GALLON = 'GAL'
    MILLILETER = 'ML'
    LITER = 'LTR'
    
    MILLIMETER = 'MM'
    CENTIMETER = 'CM'
    METER = 'MTR'
    INCH = 'IN'



    unit_type_choices = models.TypedChoiceField(

