from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	created = models.DateTimeField(auto_now_add=True)  # When this Post was written
	timestamp = models.DateTimeField(auto_now_add=True) # When this Post was REALLY written (for travels from 4/8/17-9/8/17)
	description = models.CharField(max_length=300, blank=True, default='')
	#thumbnail = 
	text = models.CharField(max_length=2000, blank=True, default='')

	class Meta:
		ordering = ('created',)
