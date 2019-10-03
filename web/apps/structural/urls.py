from django.urls import path
from . import views

app_name = 'structural'

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.get, name='get')
]
