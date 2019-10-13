from django.urls import path, include
from . import views
app_name = 'structural'

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.get, name='get'),
    path('api/offer/', views.apioffer, name='apioffer'),
]
