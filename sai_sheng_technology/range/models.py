from django.db import models

# Create your models here.
class Score(models.Model):
	name = models.CharField(max_length=30)
	score = models.CharField(max_length=10)