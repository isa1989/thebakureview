from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(db_index=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("news_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Yeniliklər"
        verbose_name_plural = "Yeniliklər"
        indexes = [
            models.Index(fields=["title", "author"]),
        ]


class Prose(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(db_index=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("prose_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Nəsr"
        verbose_name_plural = "Nəsr"
        indexes = [
            models.Index(fields=["title", "author"]),
        ]


class Poetry(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = CKEditor5Field("Text", config_name="extends", db_index=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("poetry_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Poeziya"
        verbose_name_plural = "Poeziya"
        indexes = [
            models.Index(fields=["title", "author"]),
        ]

    def first_line(self):
        return self.content.splitlines()[1] if self.content.splitlines() else ""


class Writings(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(db_index=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("writings_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Yazılar"
        verbose_name_plural = "Yazılar"
        indexes = [
            models.Index(fields=["title", "author"]),
        ]


class Interview(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    content = CKEditor5Field("Text", config_name="extends", db_index=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("interview_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Müsahibə"
        verbose_name_plural = "Müsahibə"
        indexes = [
            models.Index(fields=["title", "author"]),
        ]


class Home(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field("Text", config_name="extends")
    image = models.ImageField(upload_to="news_images/")
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    source_model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Manşet"
        verbose_name_plural = "Manşet"


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biz Kimik"
        verbose_name_plural = "Biz Kimik"


class SubmissionGuidelines(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yazı Qəbulu"
        verbose_name_plural = "Yazı Qəbulu"
