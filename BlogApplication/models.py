from django.db import models
from ckeditor.fields import RichTextField
from uuslug import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,null=True)
    category_keywords = models.CharField(max_length=255,null=True)
    category_description = models.CharField(max_length=255,null=True)
    seo_url = models.CharField(max_length=255,unique=True, null=True, blank=True,verbose_name='URL : (Auto)')
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return '{}'.format(self.category_name)
    def save(self, *args, **kwargs):
        self.seo_url = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255,null=True)
    time = models.DateTimeField(auto_now=False,null=True)
    content = RichTextField(null=True)
    keywords = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    category_list = models.ForeignKey(Category,null=True, on_delete=models.CASCADE)
    seo_url = models.CharField(max_length=255,unique=True, null=True, blank=True,verbose_name='URL : (Auto)')
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Posts"
    def __str__(self):
        return '{}'.format(self.title)
    def save(self, *args, **kwargs):
        self.seo_url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=255,null=True)
    time = models.DateTimeField(auto_now=False,null=True)
    content = RichTextField(null=True)
    keywords = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    seo_url = models.CharField(max_length=255,unique=True, null=True, blank=True,verbose_name='URL : (Auto)')
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Pages"
    def __str__(self):
        return '{}'.format(self.title)
    def save(self, *args, **kwargs):
        self.seo_url = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
