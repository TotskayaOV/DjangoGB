from django.core.management.base import BaseCommand
from myapp2.models import Client
from faker import Faker

class Command(BaseCommand):
    help = "Create clients"

    def handle(self, *args, **kwargs):
        for i in range(10):
            fake = Faker()
            client = Client(name=fake.name(),
                            email=fake.email(),
                            phone=fake.phone_number(),
                            address=fake.address())
            client.save()
            self.stdout.write(str(client.name))
