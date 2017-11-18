from rest_framework import serializers

from . import models as core_models
from django.contrib.auth import models as auth_models

class DataTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = core_models.DataTemplate
        fields = ('id', 'name', 'group', 'user', 'created', 'updated', 'fields' )

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = core_models.Tag
        fields = ('id','label', 'url','description', 'concepturi', 'created', 'updated', 'groups' )

class GroupSerializer(serializers.ModelSerializer):
    data_templates = DataTemplateSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    moderators = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = core_models.Group
        fields = ('id', 'name', 'created', 'updated', 'size', 'members', 'location', 'description', 'moderators', 'picture', 'data_templates',
                  'tags', )
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = core_models.Comment
        fields = ('id', 'owner', 'text', 'post', 'created', 'updated',)

class UserSerializer(serializers.ModelSerializer):
    joined_groups = GroupSerializer(many=True, read_only=True)
    moderated_groups = GroupSerializer(many=True, read_only=True)
    data_templates = DataTemplateSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True,) 

    class Meta:
        model = auth_models.User
        fields = ('id', 'username', 'email', 'joined_groups', 'moderated_groups', 'data_templates', 'comments', )

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=False)

    class Meta:
        model = core_models.Post
        fields = ('id', 'owner', 'text', 'group', 'data_template', 'created', 'updated', 'comments' )
