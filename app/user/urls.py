"""
URL mappings for the user API
"""
from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),

]