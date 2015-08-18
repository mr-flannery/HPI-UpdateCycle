from django.db import models

# Create your models here.

class Page(models.Model):
	name = models.CharField(max_length=200, unique=True)
	url = models.CharField(max_length=200)
	comment = models.TextField()
	contact_person = models.CharField(max_length=200)
	next_update_at = models.DateField()

	def __str__(self):
		return str(self.name)