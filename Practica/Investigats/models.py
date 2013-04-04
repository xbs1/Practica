from django.db import models

class Investigats(models.Model):
	Nom_Investigat = models.TextField(max_length=100)
	Cas = models.TextField(max_length=100)
