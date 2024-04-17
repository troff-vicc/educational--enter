from rest_framework import serializers
from .models import UserAdmins, UpdateEmployees, AddEmployees

class UserAdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmins
        fields = '__all__'

class UpdateEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateEmployees
        fields = '__all__'
        
class AddEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddEmployees
        fields = '__all__'