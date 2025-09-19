from django import forms
from .models import Vehicule, Chauffeur, Trajet, Reservation

# Formulaire de base qui applique la classe CSS Bootstrap à tous les champs
class FormulaireBootstrap(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for champ in self.fields.values():
            classes = champ.widget.attrs.get('class', '')
            champ.widget.attrs.update({'class': f'{classes} form-control'.strip()})

class VehiculeFormulaire(FormulaireBootstrap):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'marque', 'modele', 'capacite_passagers', 'statut']
        labels = {
            'immatriculation': 'Immatriculation',
            'marque': 'Marque',
            'modele': 'Modèle',
            'capacite_passagers': 'Capacité (passagers)',
            'statut': 'Statut',
        }

class ChauffeurFormulaire(FormulaireBootstrap):
    class Meta:
        model = Chauffeur
        fields = ['prenom', 'nom', 'telephone', 'numero_permis', 'statut']
        labels = {
            'prenom': 'Prénom',
            'nom': 'Nom',
            'telephone': 'Téléphone',
            'numero_permis': 'Numéro de permis',
            'statut': 'Statut',
        }

class TrajetFormulaire(FormulaireBootstrap):
    # Widgets pour le choix date/heure 
    depart_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Départ (date/heure)")
    arrivee_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Arrivée (date/heure)")

    class Meta:
        model = Trajet
        fields = ['vehicule', 'chauffeur', 'origine', 'destination', 'depart_datetime', 'arrivee_datetime', 'statut']
        labels = {
            'vehicule': 'Véhicule',
            'chauffeur': 'Chauffeur',
            'origine': 'Origine',
            'destination': 'Destination',
            'statut': 'Statut',
        }

class ReservationFormulaire(FormulaireBootstrap):
    class Meta:
        model = Reservation
        fields = ['trajet', 'nom_client', 'telephone_client', 'nombre_passagers', 'statut']
        labels = {
            'trajet': 'Trajet',
            'nom_client': 'Nom du client',
            'telephone_client': 'Téléphone du client',
            'nombre_passagers': 'Nombre de passagers',
            'statut': 'Statut',
        }