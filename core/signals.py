from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver

from .models import Home, Interview, News, Poetry, Prose, Writings


def update_home_with_new_content(instance, source_model_name):
    home_instance, created = Home.objects.get_or_create(
        source_model=source_model_name,
        defaults={
            "title": instance.title,
            "thumbnail": instance.thumbnail,
            "is_active": instance.is_active,
        },
    )

    if not created:
        home_instance.title = instance.title
        home_instance.thumbnail = instance.thumbnail
        home_instance.is_active = instance.is_active
        home_instance.save()

    home_instance.authors.set(instance.authors.all())


def delete_home_with_new_content(source_model_name):
    Home.objects.filter(source_model=source_model_name).delete()


@receiver(post_save, sender=News)
@receiver(post_save, sender=Interview)
@receiver(post_save, sender=Writings)
@receiver(post_save, sender=Poetry)
@receiver(post_save, sender=Prose)
def add_content_to_home(sender, instance, created, **kwargs):
    if not created:
        model_name = sender.__name__.lower()
        update_home_with_new_content(instance, f"{model_name}/{instance.slug}/")


@receiver(pre_delete, sender=News)
@receiver(pre_delete, sender=Interview)
@receiver(pre_delete, sender=Writings)
@receiver(pre_delete, sender=Poetry)
@receiver(pre_delete, sender=Prose)
def delete_content_from_home(sender, instance, **kwargs):
    model_name = sender.__name__.lower()
    delete_home_with_new_content(f"{model_name}/{instance.slug}/")


@receiver(m2m_changed, sender=News.authors.through)
@receiver(m2m_changed, sender=Interview.authors.through)
@receiver(m2m_changed, sender=Writings.authors.through)
@receiver(m2m_changed, sender=Poetry.authors.through)
@receiver(m2m_changed, sender=Prose.authors.through)
def authors_changed(sender, instance, action, **kwargs):
    if action in [
        "post_add",
        "post_remove",
        "post_clear",
    ]:
        model_name = instance.__class__.__name__.lower()
        update_home_with_new_content(instance, f"{model_name}/{instance.slug}/")
