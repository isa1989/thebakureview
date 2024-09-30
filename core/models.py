from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Yeniliklər"
        verbose_name_plural = "Yeniliklər"


class Prose(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Nəsr"
        verbose_name_plural = "Nəsr"


class Poetry(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field("Text", config_name="extends")
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Poeziya"
        verbose_name_plural = "Poeziya"


class Writtings(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Yazılar"
        verbose_name_plural = "Yazılar"


class Interview(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field("Text", config_name="extends")
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Müsahibə"
        verbose_name_plural = "Müsahibə"
