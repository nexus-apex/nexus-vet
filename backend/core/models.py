from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=50, choices=[("dog", "Dog"), ("cat", "Cat"), ("bird", "Bird"), ("rabbit", "Rabbit"), ("fish", "Fish"), ("reptile", "Reptile"), ("other", "Other")], default="dog")
    breed = models.CharField(max_length=255, blank=True, default="")
    age_years = models.IntegerField(default=0)
    owner_name = models.CharField(max_length=255, blank=True, default="")
    owner_phone = models.CharField(max_length=255, blank=True, default="")
    weight_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("deceased", "Deceased")], default="active")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class PetOwner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    pets_count = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    last_visit = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class VetVisit(models.Model):
    pet_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255, blank=True, default="")
    vet = models.CharField(max_length=255, blank=True, default="")
    visit_type = models.CharField(max_length=50, choices=[("checkup", "Checkup"), ("vaccination", "Vaccination"), ("surgery", "Surgery"), ("emergency", "Emergency"), ("grooming", "Grooming")], default="checkup")
    date = models.DateField(null=True, blank=True)
    diagnosis = models.TextField(blank=True, default="")
    treatment = models.TextField(blank=True, default="")
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    follow_up = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.pet_name
