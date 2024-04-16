from rest_framework import serializers
from .models import UserAdmins

class UserAdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmins
        fields = '__all__'