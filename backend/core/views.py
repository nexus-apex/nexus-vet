import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Pet, PetOwner, VetVisit


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['pet_count'] = Pet.objects.count()
    ctx['pet_dog'] = Pet.objects.filter(species='dog').count()
    ctx['pet_cat'] = Pet.objects.filter(species='cat').count()
    ctx['pet_bird'] = Pet.objects.filter(species='bird').count()
    ctx['pet_total_weight_kg'] = Pet.objects.aggregate(t=Sum('weight_kg'))['t'] or 0
    ctx['petowner_count'] = PetOwner.objects.count()
    ctx['petowner_active'] = PetOwner.objects.filter(status='active').count()
    ctx['petowner_inactive'] = PetOwner.objects.filter(status='inactive').count()
    ctx['petowner_total_total_spent'] = PetOwner.objects.aggregate(t=Sum('total_spent'))['t'] or 0
    ctx['vetvisit_count'] = VetVisit.objects.count()
    ctx['vetvisit_checkup'] = VetVisit.objects.filter(visit_type='checkup').count()
    ctx['vetvisit_vaccination'] = VetVisit.objects.filter(visit_type='vaccination').count()
    ctx['vetvisit_surgery'] = VetVisit.objects.filter(visit_type='surgery').count()
    ctx['vetvisit_total_cost'] = VetVisit.objects.aggregate(t=Sum('cost'))['t'] or 0
    ctx['recent'] = Pet.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def pet_list(request):
    qs = Pet.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(species=status_filter)
    return render(request, 'pet_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def pet_create(request):
    if request.method == 'POST':
        obj = Pet()
        obj.name = request.POST.get('name', '')
        obj.species = request.POST.get('species', '')
        obj.breed = request.POST.get('breed', '')
        obj.age_years = request.POST.get('age_years') or 0
        obj.owner_name = request.POST.get('owner_name', '')
        obj.owner_phone = request.POST.get('owner_phone', '')
        obj.weight_kg = request.POST.get('weight_kg') or 0
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/pets/')
    return render(request, 'pet_form.html', {'editing': False})


@login_required
def pet_edit(request, pk):
    obj = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.species = request.POST.get('species', '')
        obj.breed = request.POST.get('breed', '')
        obj.age_years = request.POST.get('age_years') or 0
        obj.owner_name = request.POST.get('owner_name', '')
        obj.owner_phone = request.POST.get('owner_phone', '')
        obj.weight_kg = request.POST.get('weight_kg') or 0
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/pets/')
    return render(request, 'pet_form.html', {'record': obj, 'editing': True})


@login_required
def pet_delete(request, pk):
    obj = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/pets/')


@login_required
def petowner_list(request):
    qs = PetOwner.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'petowner_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def petowner_create(request):
    if request.method == 'POST':
        obj = PetOwner()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.address = request.POST.get('address', '')
        obj.pets_count = request.POST.get('pets_count') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.status = request.POST.get('status', '')
        obj.last_visit = request.POST.get('last_visit') or None
        obj.save()
        return redirect('/petowners/')
    return render(request, 'petowner_form.html', {'editing': False})


@login_required
def petowner_edit(request, pk):
    obj = get_object_or_404(PetOwner, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.address = request.POST.get('address', '')
        obj.pets_count = request.POST.get('pets_count') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.status = request.POST.get('status', '')
        obj.last_visit = request.POST.get('last_visit') or None
        obj.save()
        return redirect('/petowners/')
    return render(request, 'petowner_form.html', {'record': obj, 'editing': True})


@login_required
def petowner_delete(request, pk):
    obj = get_object_or_404(PetOwner, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/petowners/')


@login_required
def vetvisit_list(request):
    qs = VetVisit.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(pet_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(visit_type=status_filter)
    return render(request, 'vetvisit_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def vetvisit_create(request):
    if request.method == 'POST':
        obj = VetVisit()
        obj.pet_name = request.POST.get('pet_name', '')
        obj.owner_name = request.POST.get('owner_name', '')
        obj.vet = request.POST.get('vet', '')
        obj.visit_type = request.POST.get('visit_type', '')
        obj.date = request.POST.get('date') or None
        obj.diagnosis = request.POST.get('diagnosis', '')
        obj.treatment = request.POST.get('treatment', '')
        obj.cost = request.POST.get('cost') or 0
        obj.follow_up = request.POST.get('follow_up') or None
        obj.save()
        return redirect('/vetvisits/')
    return render(request, 'vetvisit_form.html', {'editing': False})


@login_required
def vetvisit_edit(request, pk):
    obj = get_object_or_404(VetVisit, pk=pk)
    if request.method == 'POST':
        obj.pet_name = request.POST.get('pet_name', '')
        obj.owner_name = request.POST.get('owner_name', '')
        obj.vet = request.POST.get('vet', '')
        obj.visit_type = request.POST.get('visit_type', '')
        obj.date = request.POST.get('date') or None
        obj.diagnosis = request.POST.get('diagnosis', '')
        obj.treatment = request.POST.get('treatment', '')
        obj.cost = request.POST.get('cost') or 0
        obj.follow_up = request.POST.get('follow_up') or None
        obj.save()
        return redirect('/vetvisits/')
    return render(request, 'vetvisit_form.html', {'record': obj, 'editing': True})


@login_required
def vetvisit_delete(request, pk):
    obj = get_object_or_404(VetVisit, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/vetvisits/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['pet_count'] = Pet.objects.count()
    data['petowner_count'] = PetOwner.objects.count()
    data['vetvisit_count'] = VetVisit.objects.count()
    return JsonResponse(data)
