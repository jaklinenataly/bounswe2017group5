# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.shortcuts import render

from django.contrib.auth import models as auth_models
from django.contrib.auth import authenticate

from . import serializers as core_serializers
from .http import ErrorResponse

from strings import strings

### List Views BEGIN

class UserList(generics.ListAPIView):
    queryset = auth_models.User.objects.all()
    serializer_class = core_serializers.UserSerializer

class GroupList(generics.ListAPIView):
    queryset = core_models.Group.objects.all()
    serializer_class = core_serializers.GroupSerializer

class DataTemplateList(generics.ListCreateAPIView):
    queryset = data_templates_models.DataTemplate.objects.all()
    serializer_class = core_serializers.DataTemplateSerializer



### List Views END

### Detail Views BEGIN

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = auth_models.User.objects.all()
    serializer_class = core_serializers.UserSerializer

class GroupDetail(generics.RetrieveUpdateAPIView):
    queryset = core_models.Group.objects.all()
    serializer_class = core_serializers.GroupSerializer

class DataTemplateDetail(generics.RetrieveUpdateAPIView):
    queryset = data_templates_models.DataTemplate.objects.all()
    serializer_class = core_serializers.DataTemplateSerializer

### Detail Views END

