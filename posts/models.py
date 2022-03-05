from django.db import models

from django.utils import timezone
# Create your models here.


class Post(models.Model): 
	text = models.TextField()

	def __str__(self): 
		return self.text[:50]


	#datetime = models.DateTimeField(default = timezone.now)