from django.db import models

class songsDb(models.Model):
	title = models.CharField(max_length = 200)
	url = models.ListField()
	songName = models.ListField()
	author = models.ListField()
	ziplink = models.ListField()