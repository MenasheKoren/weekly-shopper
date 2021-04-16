from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import djfractions

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
    
class Recipe(models.Model):
    """Model definition for Recipe."""

    # TODO: Define fields here
    
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTIES = (
        (DIFFICULTY_EASY, 'easy'),
        (DIFFICULTY_MEDIUM, 'normal'),
        (DIFFICULTY_HARD, 'hard'),
    )
    
    
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField('Description', blank=True)
    image = models.ImageField(upload_to='img/', height_field=None, width_field=None, max_length=None)
    quantity_integer = models.PositiveSmallIntegerField('Quantity', help_text='Only positive whole numbers', null=False)
    quantity_fraction = djfractions.models.DecimalFractionField(verbose_name='Fraction',
                                        name=None,
                                        max_digits=4,
                                        decimal_places=4,
                                        limit_denominator=None,
                                        coerce_thirds=True,
                                        help_text='Optional fraction',
                                        null=True)
    ingredients = models.TextField('Ingredients', help_text='One ingredient per line')
    
    preparation = models.TextField('Preparation')
    time_for_preparation = models.DurationField('Preparation time', help_text='In minutes', blank=True, null=True)
    number_of_portions = models.PositiveIntegerField('Number of portions')
    
    difficulty = models.SmallIntegerField('Difficulty')
    category = models.ManyToManyField(Category, verbose_name='Categories')
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE,)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    
    difficulty = models.SmallIntegerField(u'Difficulty',
    choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
    

    

    class Meta:
        """Meta definition for Recipe."""

        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['-date_created']

    def __str__(self):
        """Unicode representation of Recipe."""
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Recipe, self).save(*args, **kwargs)

