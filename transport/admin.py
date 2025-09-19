from django.contrib import admin
from .models import Vehicule, Chauffeur, Trajet, Reservation

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'marque', 'modele', 'capacite_passagers', 'statut', 'date_creation')
    search_fields = ('immatriculation', 'marque', 'modele')
    list_filter = ('statut',)

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'telephone', 'numero_permis', 'statut')
    search_fields = ('prenom', 'nom', 'numero_permis')
    list_filter = ('statut',)

@admin.register(Trajet)
class TrajetAdmin(admin.ModelAdmin):
    list_display = ('origine', 'destination', 'depart_datetime', 'arrivee_datetime', 'vehicule', 'chauffeur', 'statut')
    list_filter = ('statut', 'vehicule', 'chauffeur')
    search_fields = ('origine', 'destination')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('trajet', 'nom_client', 'nombre_passagers', 'statut', 'date_creation')
    list_filter = ('statut',)
    search_fields = ('nom_client', 'trajet__origine', 'trajet__destination')