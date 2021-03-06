from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

## each class is its own table in the database 

class Post(models.Model):

	title = models.CharField(max_length=100)
	book_author = models.CharField(max_length=100)				## book author
	summary = models.TextField()								## book summary field
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True, blank=True)	## post author // one to many relationship b/t User and Post


	def __str__(self):
		return self.title 

	def get_absolute_url(self):

		return reverse('post-detail', kwargs={'pk': self.pk})
