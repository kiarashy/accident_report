from django.db import models

class AccidentReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    spam_email = models.CharField(max_length=255, null=True, blank=True)
    spam_number = models.CharField(max_length=255, null=True, blank=True)
    spam_type = models.CharField(max_length=255, null=True, blank=True)
    spam_name = models.CharField(max_length=255, null=True, blank=True)
    spam_location = models.CharField(max_length=255, null=True, blank=True)
    siren = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    vic_email = models.CharField(max_length=255, null=True, blank=True)
    vic_number = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
