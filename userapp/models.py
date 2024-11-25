from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=105)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=55)

    def __str__(self):
        return self.tag_name


class Product(models.Model):
    product_name = models.CharField(max_length=20, verbose_name='Product Name', help_text='Product Name')
    image = models.ImageField(upload_to='uploads/products')
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
