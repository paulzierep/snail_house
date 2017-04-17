from __future__ import unicode_literals

from django.db import models
import os
from schnecken_tempo.settings import MEDIA_ROOT

print MEDIA_ROOT

class figures(models.Model):
    name = models.CharField(max_length = 100)
    captiom = models.TextField()
    fig_type = models.CharField(max_length = 10)
    path = models.CharField(max_length = 100)
    #index = models.Id()

def fill_figures():
	for file in os.listdir('./'):
		pass
		#p = Person(name="Fred Flintstone", shirt_size="L")