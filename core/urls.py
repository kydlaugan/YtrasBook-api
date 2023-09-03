from django.urls import path 
from core.views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
]