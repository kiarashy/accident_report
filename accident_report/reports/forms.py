from django import forms
from .models import AccidentReport


class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = [
            'title', 'description', 'spam_email', 'spam_number', 'spam_type', 
            'spam_name', 'spam_location', 'siren', 'site', 'vic_email', 
            'vic_number', 'location'
        ]  # Include all relevant fields

