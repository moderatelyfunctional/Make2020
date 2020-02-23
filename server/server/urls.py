"""server URL Configuration

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
import threading

from django.contrib import admin
from django.urls import path

import samaritan_user.views
from samaritan_user.models import SamaritanState, SamaritanKeyDown

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', samaritan_user.views.index),
    path('send_key/', samaritan_user.views.drive),
    path('webcam/', samaritan_user.views.feed)
]

state_exists = SamaritanState.objects.exists()
if not state_exists:
    first_state = SamaritanState.objects.create(driver='default', state='nr')
    first_state.save()

key_exists = SamaritanKeyDown.objects.exists()
if not key_exists:
    first_key = SamaritanKeyDown.objects.create(left=False, right=False, forward=False, backward=False)
    first_key.save()

def fetch_keys():
    threading.Timer(5.0, fetch_keys).start()
    first_key = SamaritanKeyDown.objects.all().first()
    # print('Key is left={} right={} forward={} backward={}'.format(
    #     first_key.left, 
    #     first_key.right, 
    #     first_key.forward, 
    #     first_key.backward))

# fetch_keys()