from django.urls import path
from .views import *

urlpatterns = [
    path('user-admin/', UserAdminViews.as_view(), name='userAdmin'),
    path('update-employees/', UpdateEmployeesViews.as_view(), name='updateEmployees'),
    path('add-employees/', AddEmployeesViews.as_view(), name='addEmployees')
]