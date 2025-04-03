from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _




class AccidentReport(models.Model):
    title = models.CharField(_("Title"), max_length=255)  # 🟢 Translatable label
    description = models.TextField(_("Description"))
    
    spam_email = models.CharField(_("Spammer Email"), max_length=255, null=True, blank=True)
    spam_number = models.CharField(_("Spammer Phone Number"), max_length=255, null=True, blank=True)
    spam_type = models.CharField(_("Spam Type"), max_length=255)  # Required
    spam_name = models.CharField(_("Spammer Name"), max_length=255)  # Required
    spam_location = models.CharField(_("Spam Location"), max_length=255, null=True, blank=True)
    
    siren = models.CharField(_("SIREN Number"), max_length=255, null=True, blank=True)
    site = models.CharField(_("Website"), max_length=255, null=True, blank=True)
    vic_email = models.CharField(_("Victim Email"), max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(_("Date Reported"), auto_now_add=True)
    vote_count = models.IntegerField(_("Vote Count"), default=0)



    def __str__(self):
        return self.title
