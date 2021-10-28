from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class ProductTagModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    verbose_name = 'product tag'
    verbose_name_plural = 'product tags'


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    verbose_name = 'category'
    verbose_name_plural = 'categories'


class BrandModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'brand'
    verbose_name_plural = 'brands'


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products', verbose_name='image', null=True)
    price = models.FloatField(verbose_name='price', null=True)
    discount = models.PositiveIntegerField(default=0, verbose_name='discount', null=True)
    short_description = models.TextField(max_length=255)
    long_description = RichTextUploadingField(verbose_name='long_description', default=0)
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='products')
    brand = models.ForeignKey(BrandModel,
                              on_delete=models.PROTECT,
                              related_name='products')
    tags = models.ManyToManyField(ProductTagModel,
                                  related_name='products',
                                  verbose_name='tags')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def is_discount(self):
        return self.is_discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    def __str__(self):
        return self.title

    verbose_name = 'product'
    verbose_name_plural = 'products'


class SizeModel(models.Model):
    title = models.CharField(max_length=3, verbose_name='title', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    code = models.CharField(max_length=10, verbose_name='code', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
