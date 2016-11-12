from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# class Tokens(models.Model):
#     user = models.User
#
#     def get_absolute_url(self):
#         return(reverse('userManager:detail',kwargs={'pk':self.pk})) #keyword args
#
#     def __str__(self):
#         return self.album_title + ' - ' + self.artist