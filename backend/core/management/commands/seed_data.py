from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Pet, PetOwner, VetVisit
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusVet with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusvet.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Pet.objects.count() == 0:
            for i in range(10):
                Pet.objects.create(
                    name=f"Sample Pet {i+1}",
                    species=random.choice(["dog", "cat", "bird", "rabbit", "fish", "reptile", "other"]),
                    breed=f"Sample {i+1}",
                    age_years=random.randint(1, 100),
                    owner_name=f"Sample Pet {i+1}",
                    owner_phone=f"+91-98765{43210+i}",
                    weight_kg=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "deceased"]),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Pet records created'))

        if PetOwner.objects.count() == 0:
            for i in range(10):
                PetOwner.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    address=f"Sample address for record {i+1}",
                    pets_count=random.randint(1, 100),
                    total_spent=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "inactive"]),
                    last_visit=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 PetOwner records created'))

        if VetVisit.objects.count() == 0:
            for i in range(10):
                VetVisit.objects.create(
                    pet_name=f"Sample VetVisit {i+1}",
                    owner_name=f"Sample VetVisit {i+1}",
                    vet=f"Sample {i+1}",
                    visit_type=random.choice(["checkup", "vaccination", "surgery", "emergency", "grooming"]),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    diagnosis=f"Sample diagnosis for record {i+1}",
                    treatment=f"Sample treatment for record {i+1}",
                    cost=round(random.uniform(1000, 50000), 2),
                    follow_up=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 VetVisit records created'))
