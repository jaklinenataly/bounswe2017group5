# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
import datetime
from django.contrib.postgres.fields import JSONField
import inspect
from enum import Enum

# BaseModel, do not touch this...
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created',)


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not (m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(str(p[1].value), p[0]) for p in props])
        return choices


# Models START

class ProfilePage(BaseModel):
    name = models.CharField(max_length=30, blank=True, default='')
    surname = models.CharField(max_length=30, blank=True, default='')
    date_of_birth = models.DateField(
        blank=True, default=datetime.date(1900, 1, 1))
    location = models.TextField(blank=True, default='')
    interests = models.TextField(blank=True, default='')
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE,
                                verbose_name="user", related_name='profile')
    follows = models.ManyToManyField('ProfilePage', related_name='followed_by')


class Tag(BaseModel):
    label = models.TextField()
    url = models.URLField()
    concepturi = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.label + ' (' + self.concepturi + ')'


class Group(BaseModel):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, default='')
    location = models.TextField(blank=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, related_name='groups')
    is_private = models.BooleanField(blank=True, default=False)
    members = models.ManyToManyField(
        auth_models.User, blank=True, related_name='joined_groups')
    moderators = models.ManyToManyField(
        auth_models.User, blank=True, related_name='moderated_groups')
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def size(self):
        return self.members.count()

    def get_picture(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return '/static/assets/img/group_default_icon.png'


class Post(BaseModel):
    owner = models.ForeignKey(
        auth_models.User, related_name="posts", default=None, null=True)
    group = models.ForeignKey(
        Group, related_name='posts', on_delete=models.CASCADE, default=None, null=True)
    data_template = models.ForeignKey(
        'api.DataTemplate', related_name='posts', default=None, null=True)
    data = JSONField()

    def vote_sum(self):
        return self.votes.filter(up=True).count() - self.votes.filter(up=False).count()

    def __str__(self):
        return json.dumps(self.data)


class Comment(BaseModel):
    owner = models.ForeignKey(
        auth_models.User, related_name="comments", default=None)
    text = models.TextField(default='', blank=True)
    post = models.ForeignKey(Post, related_name='comments', default=None)

    def __str__(self):
        return self.text


class Vote(BaseModel):
    owner = models.ForeignKey(
        auth_models.User, related_name="votes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="votes",
                             on_delete=models.CASCADE)
    up = models.NullBooleanField(default=None)

    def __str__(self):
        return str(self.owner.id) + ' -> ' + str(self.post.id) + ' ' + str(self.up)

    class Meta:
        unique_together = (('owner', 'post'), )


class DataTemplate(BaseModel):
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, related_name='data_templates',
                              on_delete=models.SET_NULL, default=None, null=True)
    user = models.ForeignKey(auth_models.User, related_name='data_templates', on_delete=models.SET_NULL, default=None,
                             null=True)
    fields = JSONField()

    def __str__(self):
        return self.name

class Annotation(BaseModel):
    user = models.ForeignKey(auth_models.User, related_name='%(app_label)s_%(class)s_related', on_delete=models.SET_NULL, default=None,
                             null=True)
    text = models.TextField(default='', blank=True)
    post = models.ForeignKey(Post, related_name='%(app_label)s_%(class)s_related', default=None)
    xpath = models.CharField(max_length=40)

    class Meta:
        abstract = True

class ImageAnnotation(Annotation):
    x= models.IntegerField(blank=False)
    y= models.IntegerField(blank=False)
    w= models.IntegerField(blank=False)
    h= models.IntegerField(blank=False)

    def as_W3C(self):
        attr_tpl = (self.id, self.created, self.user.profile.id, self.user.profile.name, self.user.profile.surname, self.user.username, self.user.email, self.text, self.xpath, self.x, self.y, self.w, self.h)
        json_str = {"@context": "http://www.w3.org/ns/anno.jsonld", 
            "id": "http://interestr.com/annotations/" + str(self.id), 
            "type": "Annotation",
            "created": self.created,
            "creator": {
            "id": "http://interestr.com/profile/" + str(self.user.profile.id),
            "type": "Person",
            "name":  self.user.profile.name + " " +  str(self.user.profile.surname),
            "nickname": self.user.username ,
            "email": self.user.email
                },

            "bodyValue": self.text,
            "target": {
            "source": "http://interestr.com/posts/" + str(self.post.id),
                "type": "Image",
             "selector": {
              "type": "XPathSelector",
              "value": self.xpath,
                  "refinedBy": {
                          "type": "FragmentSelector",
                          "conformsTo": "http://www.w3.org/TR/media-frags/",
                          "value": "xywh=" + str(self.x) + "," + str(self.y)+ "," + str(self.w)+ "," + str(self.h) 

            }  
            }
            }

            }
        return json_str

        


class TextAnnotation(Annotation):
    start= models.IntegerField(blank=False)
    end= models.IntegerField(blank=False)

    def as_W3C(self):
        json_str = {"@context": "http://www.w3.org/ns/anno.jsonld", 
            "id": "http://interestr.com/annotations/" + str(self.id), 
            "type": "Annotation",
            "created": self.created,
            "creator": {
            "id": "http://interestr.com/profile/" + str(self.user.profile.id),
            "type": "Person",
            "name":  self.user.profile.name + " " +  str(self.user.profile.surname),
            "nickname": self.user.username ,
            "email": self.user.email
                },

            "bodyValue": self.text,
            "target": {
            "source": "http://interestr.com/posts/" + str(self.post.id),
                "type": "Text",
             "selector": {
              "type": "XPathSelector",
              "value": self.xpath,
	  "refinedBy": {
		  "type": "TextPositionSelector",
		  "start": self.start,
		  "end": self.end
    }   
            }
            }

            }
        return json_str



# Models END
