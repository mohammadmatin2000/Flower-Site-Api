from django.core.management.base import BaseCommand
from ...models import PlantProduct, PlantCategory, PlantImage
from faker import Faker
from django.utils.text import slugify
import random
from django.core.files.base import ContentFile
import requests


# ======================================================================================================================
class Command(BaseCommand):
    help = "Generate fake PlantProduct data with Persian names"

    def handle(self, *args, **kwargs):
        fake = Faker("fa_IR")

        categories = list(PlantCategory.objects.all())
        if not categories:
            self.stdout.write(
                self.style.ERROR("هیچ دسته‌بندی‌ای وجود ندارد! اول دسته‌بندی‌ها را بسازید.")
            )
            return

        PLANT_TYPES = [choice[0] for choice in PlantProduct.PLANT_TYPES]
        PLANT_STATUS = [choice[0] for choice in PlantProduct.status.field.choices]

        for _ in range(10):
            category = random.choice(categories)
            name = fake.word()
            slug = slugify(name, allow_unicode=True)
            scientific_name = fake.word() + " " + fake.word()
            plant_type = random.choice(PLANT_TYPES)
            description = fake.paragraph(nb_sentences=5)
            care_instructions = fake.paragraph(nb_sentences=3)
            height_cm = round(random.uniform(10, 200), 1)
            price = round(random.uniform(20000, 500000), 2)
            discount_percent = random.choice([0, 5, 10, 15, 20, None])
            stock = random.randint(0, 50)
            status = random.choice(PLANT_STATUS)

            product = PlantProduct.objects.create(
                category=category,
                name=name,
                slug=slug,
                scientific_name=scientific_name,
                plant_type=plant_type,
                description=description,
                care_instructions=care_instructions,
                height_cm=height_cm,
                price=price,
                discount_percent=discount_percent,
                stock=stock,
                status=status,
            )

            # اضافه کردن تصویر فیک از اینترنت (مثال از picsum.photos)
            try:
                image_url = "https://picsum.photos/400/400"
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_name = f"{slug}.jpg"
                    product_image = PlantImage(
                        product=product,
                    )
                    product_image.image.save(
                        image_name, ContentFile(response.content), save=True
                    )
                    product_image.alt_text = f"تصویر محصول {name}"
                    product_image.save()
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f"تصویر برای محصول {name} ذخیره نشد: {e}")
                )

        self.stdout.write(self.style.SUCCESS("۱۰ محصول گیاهی فیک ساخته شد"))


# ======================================================================================================================
