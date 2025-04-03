from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AccidentReport


class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = [
            'title', 'description',
            'spam_email', 'spam_number', 'spam_type', 'spam_name', 'spam_location',
            'siren', 'site', 'vic_email',
        ]

        labels = {
            'title': "Titre",
            'description': "Description",
            'spam_email': "Email de l'arnaqueur",
            'spam_number': "Téléphone de l'arnaqueur",
            'spam_type': "Type de spam",
            'spam_name': "Nom de l'arnaqueur",
            'spam_location': "Lieu de l'arnaque",
            'siren': "Numéro SIREN",
            'site': "Site concerné",
            'vic_email': "Votre email (optionnel)",
        }
        help_texts = {
            'spam_email': _("Enter the spammer's email if known."),
            'siren': _("Optional: French SIREN company identifier."),
            'site': _("URL or domain where the spam was seen."),
        }