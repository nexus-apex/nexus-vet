from django.contrib import admin
from .models import Pet, PetOwner, VetVisit

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "breed", "age_years", "owner_name", "created_at"]
    list_filter = ["species", "status"]
    search_fields = ["name", "breed", "owner_name"]

@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "pets_count", "total_spent", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]

@admin.register(VetVisit)
class VetVisitAdmin(admin.ModelAdmin):
    list_display = ["pet_name", "owner_name", "vet", "visit_type", "date", "created_at"]
    list_filter = ["visit_type"]
    search_fields = ["pet_name", "owner_name", "vet"]
