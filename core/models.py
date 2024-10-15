import os

from django.core.files.storage import default_storage
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from PIL import Image


def create_thumbnail(image_path, thumbnail_path, size=(600, 600)):
    thumbnail_dir = os.path.dirname(thumbnail_path)

    if not os.path.exists(thumbnail_dir):
        os.makedirs(thumbnail_dir)

    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    try:
        with Image.open(image_path) as img:
            img.thumbnail(size)
            img.convert("RGB").save(thumbnail_path, "JPEG")
    except Exception as e:
        print(f"An error occurred while creating thumbnail: {e}")


def get_image_upload_thumbnail(instance, filename):
    model_name = instance.__class__.__name__.lower()
    base, ext = os.path.splitext(filename)
    return os.path.join("media", "thumbnails", model_name, f"{base}.jpeg")


def get_image_upload_path(instance, filename):
    model_name = instance.__class__.__name__.lower()
    return os.path.join("media", model_name, filename)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Müəllif"
        verbose_name_plural = "Müəlliflər"


class BaseModel(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = CKEditor5Field("Text", config_name="extends")
    image = models.ImageField(upload_to=get_image_upload_path)
    thumbnail = models.ImageField(
        upload_to=get_image_upload_path, null=True, blank=True
    )
    authors = models.ManyToManyField(
        Author, related_name="%(class)s_authors", blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_slug()
        super().save(*args, **kwargs)
        if self.image:
            image_path = self.image.path
            thumbnail_path = get_image_upload_thumbnail(self, self.image.name)
            create_thumbnail(image_path, thumbnail_path)
            self.thumbnail = os.path.relpath(thumbnail_path, start="media")
            super().save(update_fields=["thumbnail"])

    def delete(self, *args, **kwargs):
        if self.image:
            if default_storage.exists(self.image.name):
                default_storage.delete(self.image.name)

        if self.thumbnail:
            thumbnail_path = self.thumbnail.path
            if default_storage.exists(thumbnail_path):
                default_storage.delete(thumbnail_path)

        super().delete(*args, **kwargs)

    def create_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug


class News(BaseModel):
    def __str__(self):
        authors_list = ", ".join(str(author) for author in self.authors.all())
        return (
            f"{self.title} by {authors_list}" if self.authors.exists() else self.title
        )

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])

    class Meta:
        verbose_name = "Yeniliklər"
        verbose_name_plural = "Yeniliklər"


class Prose(BaseModel):
    def __str__(self):
        authors_list = ", ".join(str(author) for author in self.authors.all())
        return (
            f"{self.title} by {authors_list}" if self.authors.exists() else self.title
        )

    def get_absolute_url(self):
        return reverse("prose_detail", args=[self.slug])

    class Meta:
        verbose_name = "Nəsr"
        verbose_name_plural = "Nəsr"


class Poetry(BaseModel):

    def __str__(self):
        authors_list = ", ".join(str(author) for author in self.authors.all())
        return (
            f"{self.title} by {authors_list}" if self.authors.exists() else self.title
        )

    def get_absolute_url(self):
        return reverse("poetry_detail", args=[self.slug])

    class Meta:
        verbose_name = "Poeziya"
        verbose_name_plural = "Poeziya"


class Writings(BaseModel):
    def __str__(self):
        authors_list = ", ".join(str(author) for author in self.authors.all())
        return (
            f"{self.title} by {authors_list}" if self.authors.exists() else self.title
        )

    def get_absolute_url(self):
        return reverse("writings_detail", args=[self.slug])

    class Meta:
        verbose_name = "Yazılar"
        verbose_name_plural = "Yazılar"


class Interview(BaseModel):

    def __str__(self):
        authors_list = ", ".join(str(author) for author in self.authors.all())
        return (
            f"{self.title} by {authors_list}" if self.authors.exists() else self.title
        )

    def get_absolute_url(self):
        return reverse("interview_detail", args=[self.slug])

    class Meta:
        verbose_name = "Müsahibə"
        verbose_name_plural = "Müsahibə"


class Home(models.Model):
    title = models.CharField(max_length=200)
    # content = CKEditor5Field("Text", config_name="extends")
    thumbnail = models.ImageField(upload_to=get_image_upload_thumbnail)
    authors = models.ManyToManyField(Author, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    source_model = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Manşet"
        verbose_name_plural = "Manşet"


class AboutUs(models.Model):
    # title = models.CharField(max_length=200)
    # content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Biz Kimik"
        verbose_name_plural = "Biz Kimik"


class SubmissionGuidelines(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field("Text", config_name="extends")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yazı Qəbulu"
        verbose_name_plural = "Yazı Qəbulu"
