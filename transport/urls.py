from django.urls import path
from . import views

urlpatterns = [
    # Accueil / Tableau de bord
    path('', views.AccueilVue.as_view(), name='accueil'),

    # Véhicules
    path('vehicules/', views.VehiculeListeVue.as_view(), name='vehicule_liste'),
    path('vehicules/ajouter/', views.VehiculeCreationVue.as_view(), name='vehicule_ajouter'),
    path('vehicules/<int:pk>/', views.VehiculeDetailVue.as_view(), name='vehicule_detail'),
    path('vehicules/<int:pk>/modifier/', views.VehiculeMiseAJourVue.as_view(), name='vehicule_modifier'),
    path('vehicules/<int:pk>/supprimer/', views.VehiculeSuppressionVue.as_view(), name='vehicule_supprimer'),

    # Chauffeurs
    path('chauffeurs/', views.ChauffeurListeVue.as_view(), name='chauffeur_liste'),
    path('chauffeurs/ajouter/', views.ChauffeurCreationVue.as_view(), name='chauffeur_ajouter'),
    path('chauffeurs/<int:pk>/', views.ChauffeurDetailVue.as_view(), name='chauffeur_detail'),
    path('chauffeurs/<int:pk>/modifier/', views.ChauffeurMiseAJourVue.as_view(), name='chauffeur_modifier'),
    path('chauffeurs/<int:pk>/supprimer/', views.ChauffeurSuppressionVue.as_view(), name='chauffeur_supprimer'),

    # Trajets
    path('trajets/', views.TrajetListeVue.as_view(), name='trajet_liste'),
    path('trajets/ajouter/', views.TrajetCreationVue.as_view(), name='trajet_ajouter'),
    path('trajets/<int:pk>/', views.TrajetDetailVue.as_view(), name='trajet_detail'),
    path('trajets/<int:pk>/modifier/', views.TrajetMiseAJourVue.as_view(), name='trajet_modifier'),
    path('trajets/<int:pk>/supprimer/', views.TrajetSuppressionVue.as_view(), name='trajet_supprimer'),

    # Réservations
    path('reservations/', views.ReservationListeVue.as_view(), name='reservation_liste'),
    path('reservations/ajouter/', views.ReservationCreationVue.as_view(), name='reservation_ajouter'),
    path('reservations/<int:pk>/', views.ReservationDetailVue.as_view(), name='reservation_detail'),
    path('reservations/<int:pk>/modifier/', views.ReservationMiseAJourVue.as_view(), name='reservation_modifier'),
    path('reservations/<int:pk>/supprimer/', views.ReservationSuppressionVue.as_view(), name='reservation_supprimer'),
]