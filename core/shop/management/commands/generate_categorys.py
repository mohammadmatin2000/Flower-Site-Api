from django.core.management.base import BaseCommand
from ...models import PlantCategory
from django.utils.text import slugify
# ======================================================================================================================
class Command(BaseCommand):
    help = "Generate fake categories"

    def handle(self, *args, **kwargs):
        categories = ['گل رز', 'کاکتوس', 'ساکولنت', 'گل آپارتمانی']
        for cat in categories:
            slug = slugify(cat, allow_unicode=True)
            PlantCategory.objects.get_or_create(title=cat, slug=slug)
        self.stdout.write(self.style.SUCCESS("Categories created"))
# ======================================================================================================================
