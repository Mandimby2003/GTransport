from django.db import models
from django.core.exceptions import ValidationError

# Modèle abstrait pour ajouter automatiquement la date de création et de mise à jour
class Horodatage(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Représente un véhicule de la flotte
class Vehicule(Horodatage):
    STATUTS = [
        ('disponible', 'Disponible'),
        ('maintenance', 'Maintenance'),
    ]

    immatriculation = models.CharField(max_length=30, unique=True)  # Ex: DK-1234-AB
    marque = models.CharField(max_length=50, blank=True)            # Ex: Toyota
    modele = models.CharField(max_length=50, blank=True)            # Ex: Hiace
    capacite_passagers = models.PositiveIntegerField(default=0)     # Nombre de places
    statut = models.CharField(max_length=20, choices=STATUTS, default='disponible')

    def __str__(self):
        # Affichage lisible dans l’admin et ailleurs
        return f"{self.immatriculation} ({self.marque} {self.modele})"

# Représente un chauffeur
class Chauffeur(Horodatage):
    STATUTS = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    ]

    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=30, blank=True)
    numero_permis = models.CharField(max_length=50, blank=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='actif')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Représente un trajet planifié (véhicule + chauffeur + origine/destination + horaires)
class Trajet(Horodatage):
    STATUTS = [
        ('planifie', 'Planifié'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]

    vehicule = models.ForeignKey(Vehicule, on_delete=models.PROTECT)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.PROTECT)
    origine = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    depart_datetime = models.DateTimeField()
    arrivee_datetime = models.DateTimeField()
    statut = models.CharField(max_length=20, choices=STATUTS, default='planifie')

    def clean(self):
        # Validation métier côté serveur
        erreurs = {}
        if self.arrivee_datetime and self.depart_datetime and self.arrivee_datetime <= self.depart_datetime:
            erreurs['arrivee_datetime'] = "La date/heure d'arrivée doit être après le départ."
        if self.vehicule and self.vehicule.statut == 'maintenance':
            erreurs['vehicule'] = "Ce véhicule est en maintenance."
        if self.chauffeur and self.chauffeur.statut != 'actif':
            erreurs['chauffeur'] = "Ce chauffeur est inactif."
        if erreurs:
            raise ValidationError(erreurs)

    def __str__(self):
        return f"{self.origine} → {self.destination} ({self.depart_datetime:%Y-%m-%d %H:%M})"

# Représente une réservation de places sur un trajet
class Reservation(Horodatage):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ]

    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reservations')
    nom_client = models.CharField(max_length=100)
    telephone_client = models.CharField(max_length=30, blank=True)
    nombre_passagers = models.PositiveIntegerField(default=1)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')

    def clean(self):
        # Empêche de dépasser la capacité du véhicule
        if self.trajet_id and self.nombre_passagers:
            deja_reserve = self.trajet.reservations.exclude(pk=self.pk).aggregate(
                total=models.Sum('nombre_passagers')
            )['total'] or 0
            capacite = self.trajet.vehicule.capacite_passagers or 0
            if deja_reserve + self.nombre_passagers > capacite:
                raise ValidationError({
                    "nombre_passagers": f"Capacité dépassée: {deja_reserve + self.nombre_passagers}/{capacite}."
                })

    def __str__(self):
        return f"Réservation {self.nom_client} x{self.nombre_passagers}"