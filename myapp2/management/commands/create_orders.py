from django.core.management.base import BaseCommand
from myapp2.models import Product, Client, Order
from random import choice, randint

class Command(BaseCommand):
    help = "Создание заказов"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(10):
            product = choice(products)
            counts = randint(1, 3)
            order = Order(
                client_id=choice(clients),
                cost=product.price * counts
            )
            order.save()
            order.product_id.set([product])
            self.stdout.write(str(order))
