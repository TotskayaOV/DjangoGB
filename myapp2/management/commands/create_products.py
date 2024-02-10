from django.core.management.base import BaseCommand
from myapp2.models import Product
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create clients"

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(name=f'Product №{i}',
                              description=" ".join(lorem_ipsum.paragraphs(2, common=False)),
                              price=(10.10 + i*i),
                              count=(100-i*2))

            product.save()
            self.stdout.write(str(product.name))
