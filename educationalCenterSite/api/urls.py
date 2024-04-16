from django.urls import path
from .views import *

urlpatterns = [
    path('user-admin/', UserAdminViews.as_view(), name='userAdmin')
]