from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True) #Categoty URL
    description = models.TextField(max_length=255, blank=True)
    # If we are using image field we need to install pillow module
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) # blank = True is optional

    class Meta:
        verbose_name = 'Category'
        # In admin, django appends 's' to model name. To get rid of that we can create a verbose plural name.
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
