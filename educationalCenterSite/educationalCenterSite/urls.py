"""
URL configuration for educationalCenterSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='referenceInformation'),
    path('applications/', views.application, name='applications'),
    path('protocols/', views.protocols, name='protocols'),
    path('reporting/', views.information, name='reporting'),
    path('information/users', views.users, name='users'),
    path('information/company', views.company, name='company'),
    path('login/', views.login, name='login'),
    path('information/employees/', views.employees, name='employees'),
    path('information/group-reports/', views.groupReports, name='groupReports'),
    path('information/studying-program/', views.studyingProgram, name='studyingProgram'),
    path('applications/clients/', views.clients, name='clients'),
    path('applications/list/', views.applicationsList, name='applicationsList'),
    path('applications/list/clients', views.listClients, name='applicationsListClients'),
    path('applications/list/install/<int:id>', views.installAccount, name='installAccount'),
    path('protocols/clients', views.protocolsClients, name='protocolsClient'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
]