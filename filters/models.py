from django.db import models
from cloudinary.models import CloudinaryField

class Pic(models.Model):
	image = CloudinaryField('image')


