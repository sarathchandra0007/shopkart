from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    # Slug field automatically creates cat url for a category
    slug = models.SlugField(max_length=100, unique=True) #Categoty URL
    description = models.TextField(max_length=255, blank=True)
    # If we are using image field we need to install pillow module
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) # blank = True is optional

    class Meta:
        verbose_name = 'Category'
        # In admin, django appends 's' to model name. To get rid of that we can create a verbose plural name.
        verbose_name_plural = 'Categories'

    def get_slug_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
