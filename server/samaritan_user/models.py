from django.db import models

# Create your models here.
STATE_CHOICES = (
	('nr', 'no-request'),
	('wd', 'waiting-for-driver'),
	('cd', 'currently-driving')
)

class SamaritanState(models.Model):
	driver = models.CharField('driver', max_length=20, unique=True)
	state = models.CharField('nr', max_length=2, choices=STATE_CHOICES)

class SamaritanKeyDown(models.Model):
	left = models.BooleanField('left', default=False)
	right = models.BooleanField('right', default=False)
	forward = models.BooleanField('forward', default=False)
	backward = models.BooleanField('backward', default=False)

