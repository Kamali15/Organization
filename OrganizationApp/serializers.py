from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Organization
        fields = '__all__'

class SubOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model =SubOrganization
        fields = '__all__'

class DivSerializer(serializers.ModelSerializer):
    class Meta:
        model =Division
        fields = '__all__'
        
class SubdivSerializer(serializers.ModelSerializer):
    class Meta:
        model =Division
        fields = '__all__'

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'