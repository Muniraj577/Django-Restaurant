from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = AutoSlugField(max_length=40, populate_from='name', unique_with='name', unique=True)
    image = models.ImageField(upload_to='category/images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('frontend:dish_by_category', args=[self.slug])



