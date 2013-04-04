from django.db import models

class Clients(models.Model):
	Nom_client = models.TextField(max_length=100)
