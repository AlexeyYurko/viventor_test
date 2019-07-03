"""viventor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from api import views as api_views
from contacts import views as contacts_views

router = routers.DefaultRouter()
router.register(r'contacts', api_views.ContactViewSet)
router.register(r'webhooks', api_views.HookViewSet, 'webhook')

urlpatterns = [
    path('', contacts_views.ContactsList.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('contacts/', contacts_views.ContactsList.as_view(), name='contact-list'),
    path('add_contact/', contacts_views.new_contact, name='new-contact'),
]
