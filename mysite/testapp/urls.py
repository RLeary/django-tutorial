from django.urls import path
from . import views

urlpatterns = [
    path('', views.testapp_index, name='testapp_index'), 
]