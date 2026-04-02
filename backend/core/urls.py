from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/create/', views.pet_create, name='pet_create'),
    path('pets/<int:pk>/edit/', views.pet_edit, name='pet_edit'),
    path('pets/<int:pk>/delete/', views.pet_delete, name='pet_delete'),
    path('petowners/', views.petowner_list, name='petowner_list'),
    path('petowners/create/', views.petowner_create, name='petowner_create'),
    path('petowners/<int:pk>/edit/', views.petowner_edit, name='petowner_edit'),
    path('petowners/<int:pk>/delete/', views.petowner_delete, name='petowner_delete'),
    path('vetvisits/', views.vetvisit_list, name='vetvisit_list'),
    path('vetvisits/create/', views.vetvisit_create, name='vetvisit_create'),
    path('vetvisits/<int:pk>/edit/', views.vetvisit_edit, name='vetvisit_edit'),
    path('vetvisits/<int:pk>/delete/', views.vetvisit_delete, name='vetvisit_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
