from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from core.models import Home, Interview, Poetry, Prose, Writings
from core.utils import create_thumbnail


def update_home_with_new_content(instance, source_model_name):
    home_instance, created = Home.objects.get_or_create(
        slug=instance.slug,
        defaults={
            "title": instance.title,
            "content": instance.content,
            "thumbnail": instance.thumbnail,
            "author": instance.author,
            "is_active": instance.is_active,
            "source_model": source_model_name,
        },
    )

    if not created:
        home_instance.title = instance.title
        home_instance.content = instance.content
        home_instance.thumbnail = instance.thumbnail
        home_instance.author = instance.author
        home_instance.is_active = instance.is_active
        home_instance.source_model = source_model_name
        home_instance.save()

    if Home.objects.count() > 20:
        oldest_home_content = Home.objects.order_by("created_at").first()
        oldest_home_content.delete()


def delete_home_with_new_content(instance, source_model_name):
    Home.objects.filter(source_model=source_model_name).delete()


@receiver(post_save, sender=Interview)
def add_interview_to_home(sender, instance, created, **kwargs):
    if created:
        update_home_with_new_content(instance, f"interviews/{instance.slug}/")


@receiver(post_save, sender=Writings)
def add_writings_to_home(sender, instance, created, **kwargs):
    if created:
        update_home_with_new_content(instance, f"writings/{instance.slug}/")


@receiver(post_save, sender=Poetry)
def add_poetry_to_home(sender, instance, created, **kwargs):
    if created:
        update_home_with_new_content(instance, f"poetry/{instance.slug}/")


@receiver(post_save, sender=Prose)
def add_prose_to_home(sender, instance, created, **kwargs):
    if instance and not created:
        update_home_with_new_content(instance, f"fiction/{instance.slug}/")


@receiver(pre_delete, sender=Interview)
def delete_interview_to_home(sender, instance, **kwargs):
    delete_home_with_new_content(instance, f"interviews/{instance.slug}/")


@receiver(pre_delete, sender=Writings)
def delete_writings_to_home(sender, instance, **kwargs):
    delete_home_with_new_content(instance, f"writings/{instance.slug}/")


@receiver(pre_delete, sender=Poetry)
def delete_poetry_to_home(sender, instance, **kwargs):
    delete_home_with_new_content(instance, f"poetry/{instance.slug}/")


@receiver(pre_delete, sender=Prose)
def delete_prose_to_home(sender, instance, **kwargs):
    delete_home_with_new_content(instance, f"fiction/{instance.slug}/")
