from django.db import models
from cloudinary.models import CloudinaryField

class Pic(models.Model):
	name = models.CharField(max_length=100, default='car')

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name



