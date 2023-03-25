from django.contrib.auth.models import User
from django.db import models

CATEGORIES = (('service', 'Service'),
              ('product', 'Product'),
              ('other', 'Other')
              )


class Product(models.Model):
    name = models.CharField(max_length=48, null=False, verbose_name='Product')
    category = models.CharField(choices=CATEGORIES, verbose_name='Category', default='other', max_length=512)
    description = models.CharField(null=True, max_length=1024, verbose_name='Description', blank=True)
    image = models.CharField(max_length=1024, null=True, verbose_name='Image',
                             default='https://www.ncenet.com/wp-content/uploads/2020/04/no-image-png-2.png')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Author')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Product')
    text = models.TextField(max_length=1024, null=False, verbose_name='Text')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.author.username} - {self.product.name}'
