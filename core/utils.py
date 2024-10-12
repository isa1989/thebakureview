import os

from PIL import Image


def get_image_upload_thumbnail(instance, filename):
    model_name = instance.__class__.__name__.lower()
    base, ext = os.path.splitext(filename)
    return os.path.join("media", "thumbnails", model_name, f"{base}.jpeg")


def get_image_upload_path(instance, filename):
    model_name = instance.__class__.__name__.lower()
    return os.path.join("media", model_name, filename)


def create_thumbnail(image_path, thumbnail_path, size=(600, 600)):
    thumbnail_dir = os.path.dirname(thumbnail_path)

    if not os.path.exists(thumbnail_dir):
        os.makedirs(thumbnail_dir)

    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    try:
        with Image.open(image_path) as img:
            # Görseli 600x600 boyutuna göre yeniden boyutlandır
            img.thumbnail(size)
            img.convert("RGB").save(thumbnail_path, "JPEG")
    except Exception as e:
        print(f"An error occurred while creating thumbnail: {e}")
