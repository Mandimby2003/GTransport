from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehicule, Chauffeur, Trajet, Reservation
from .forms import VehiculeFormulaire, ChauffeurFormulaire, TrajetFormulaire, ReservationFormulaire

# Tableau de bord (page d'accueil)
class AccueilVue(TemplateView):
    template_name = 'transport/accueil.html'

    def get_context_data(self, **kwargs):
        # Fournit des statistiques et des listes récentes pour l'accueil
        contexte = super().get_context_data(**kwargs)
        contexte['statistiques'] = {
            'vehicules': Vehicule.objects.count(),
            'chauffeurs': Chauffeur.objects.count(),
            'trajets': Trajet.objects.count(),
            'reservations': Reservation.objects.count(),
        }
        contexte['derniers_trajets'] = Trajet.objects.order_by('-date_creation')[:5]
        contexte['dernieres_reservations'] = Reservation.objects.select_related('trajet').order_by('-date_creation')[:5]
        return contexte

# Classe de base pour les listes (pagination + ordre)
class ListeBaseVue(ListView):
    paginate_by = 10
    ordering = '-date_creation'

# Vues Véhicule
class VehiculeListeVue(ListeBaseVue):
    model = Vehicule
    template_name = 'transport/vehicule_liste.html'

class VehiculeDetailVue(DetailView):
    model = Vehicule
    template_name = 'transport/vehicule_detail.html'

class VehiculeCreationVue(CreateView):
    model = Vehicule
    form_class = VehiculeFormulaire
    template_name = 'transport/vehicule_formulaire.html'
    success_url = reverse_lazy('vehicule_liste')
    def form_valid(self, form):
        messages.success(self.request, "Véhicule créé avec succès.")
        return super().form_valid(form)

class VehiculeMiseAJourVue(UpdateView):
    model = Vehicule
    form_class = VehiculeFormulaire
    template_name = 'transport/vehicule_formulaire.html'
    success_url = reverse_lazy('vehicule_liste')
    def form_valid(self, form):
        messages.success(self.request, "Véhicule mis à jour.")
        return super().form_valid(form)

class VehiculeSuppressionVue(DeleteView):
    model = Vehicule
    template_name = 'transport/vehicule_confirmation_suppression.html'
    success_url = reverse_lazy('vehicule_liste')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Véhicule supprimé.")
        return super().delete(request, *args, **kwargs)

# Vues Chauffeur
class ChauffeurListeVue(ListeBaseVue):
    model = Chauffeur
    template_name = 'transport/chauffeur_liste.html'

class ChauffeurDetailVue(DetailView):
    model = Chauffeur
    template_name = 'transport/chauffeur_detail.html'

class ChauffeurCreationVue(CreateView):
    model = Chauffeur
    form_class = ChauffeurFormulaire
    template_name = 'transport/chauffeur_formulaire.html'
    success_url = reverse_lazy('chauffeur_liste')
    def form_valid(self, form):
        messages.success(self.request, "Chauffeur créé.")
        return super().form_valid(form)

class ChauffeurMiseAJourVue(UpdateView):
    model = Chauffeur
    form_class = ChauffeurFormulaire
    template_name = 'transport/chauffeur_formulaire.html'
    success_url = reverse_lazy('chauffeur_liste')
    def form_valid(self, form):
        messages.success(self.request, "Chauffeur mis à jour.")
        return super().form_valid(form)

class ChauffeurSuppressionVue(DeleteView):
    model = Chauffeur
    template_name = 'transport/chauffeur_confirmation_suppression.html'
    success_url = reverse_lazy('chauffeur_liste')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Chauffeur supprimé.")
        return super().delete(request, *args, **kwargs)

# Vues Trajet
class TrajetListeVue(ListeBaseVue):
    model = Trajet
    template_name = 'transport/trajet_liste.html'

class TrajetDetailVue(DetailView):
    model = Trajet
    template_name = 'transport/trajet_detail.html'

class TrajetCreationVue(CreateView):
    model = Trajet
    form_class = TrajetFormulaire
    template_name = 'transport/trajet_formulaire.html'
    success_url = reverse_lazy('trajet_liste')
    def form_valid(self, form):
        messages.success(self.request, "Trajet créé.")
        return super().form_valid(form)

class TrajetMiseAJourVue(UpdateView):
    model = Trajet
    form_class = TrajetFormulaire
    template_name = 'transport/trajet_formulaire.html'
    success_url = reverse_lazy('trajet_liste')
    def form_valid(self, form):
        messages.success(self.request, "Trajet mis à jour.")
        return super().form_valid(form)

class TrajetSuppressionVue(DeleteView):
    model = Trajet
    template_name = 'transport/trajet_confirmation_suppression.html'
    success_url = reverse_lazy('trajet_liste')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Trajet supprimé.")
        return super().delete(request, *args, **kwargs)

# Vues Réservation
class ReservationListeVue(ListeBaseVue):
    model = Reservation
    template_name = 'transport/reservation_liste.html'

class ReservationDetailVue(DetailView):
    model = Reservation
    template_name = 'transport/reservation_detail.html'

class ReservationCreationVue(CreateView):
    model = Reservation
    form_class = ReservationFormulaire
    template_name = 'transport/reservation_formulaire.html'
    success_url = reverse_lazy('reservation_liste')
    def get_initial(self):
        # Pré-remplit le trajet si on arrive depuis la page d’un trajet (?trajet=ID)
        initial = super().get_initial()
        trajet_id = self.request.GET.get('trajet')
        if trajet_id:
            initial['trajet'] = trajet_id
        return initial
    def form_valid(self, form):
        messages.success(self.request, "Réservation créée.")
        return super().form_valid(form)

class ReservationMiseAJourVue(UpdateView):
    model = Reservation
    form_class = ReservationFormulaire
    template_name = 'transport/reservation_formulaire.html'
    success_url = reverse_lazy('reservation_liste')
    def form_valid(self, form):
        messages.success(self.request, "Réservation mise à jour.")
        return super().form_valid(form)

class ReservationSuppressionVue(DeleteView):
    model = Reservation
    template_name = 'transport/reservation_confirmation_suppression.html'
    success_url = reverse_lazy('reservation_liste')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Réservation supprimée.")
        return super().delete(request, *args, **kwargs)