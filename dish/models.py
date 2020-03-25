from django.db import models
from autoslug import AutoSlugField
from Category.models import Category
from django.urls import reverse
# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dish/images')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'

    def get_absolute_url(self):
        return reverse('dish:edit', args=[str(self.id)])

    def get_url(self):
        return reverse('dish:delete', args=[str(self.id)])


