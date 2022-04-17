from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Itineraire(models.Model):
    titre = models.CharField(max_length=200)
    point_depart = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    altitude_depart = models.IntegerField()
    altitude_min = models.IntegerField()
    altitude_max = models.IntegerField()
    denivele_neg = models.IntegerField()
    denivele_pos = models.IntegerField()
    duree_estimee = models.IntegerField()
    difficulte_estimee = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    def __str__(self):
        return self.titre
