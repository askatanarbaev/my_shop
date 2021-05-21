from django.db import models

CATEGORY = (
    ('building tool', 'building tool'),
    ('formwork', 'formwork'),
    ('scaffs', 'scaffs'),
    ('stoika', 'stoika'),
)

class Product(models.Model):
    name = models.CharField(choices=CATEGORY, default='', max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, verbose_name='image')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self) -> str:
        return self.name

