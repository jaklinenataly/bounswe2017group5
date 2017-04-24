# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
     author = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE)
     text = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
      # a field for comments is needed	
     class Meta:
    	ordering = ('created',)
