from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from core.models import Home, Interview, Poetry, Prose, Writings


def update_home_with_new_content(instance, source_model_name):
    Home.objects.create(
        title=instance.title,
        content=instance.content,
        image=instance.image,
        author=instance.author,
        is_active=instance.is_active,
        source_model=source_model_name,
    )

    if Home.objects.count() > 21:
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
    if created:
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
