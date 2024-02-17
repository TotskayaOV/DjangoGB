from django.core.management.base import BaseCommand
from myapp2.models import Order, Client


class Command(BaseCommand):
    help = "Search all orders by Client"

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str, help='Client Name')

    def handle(self, *args, **kwargs):
        client_name = kwargs['client_name']
        orders = Order.objects.filter(client_id__name__icontains=client_name)
        for order in orders:
            self.stdout.write(str(order))
        return orders
