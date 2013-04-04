from django.db import models

class Cas(models.Model):
	Nom_cas = models.TextField(max_length=100)
	data = models.DateTimeField()
	client = models.TextField(max_length=100)
	preu = models.IntegerField()
