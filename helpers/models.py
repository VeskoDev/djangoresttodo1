from django.db import models



class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """Stavljamo na abstractu klasu na True jer nema logike da se od ove klase prave instance, ordering ako stavimo minus ide desc"""
        abstract = True
        ordering = ('-created_at',)