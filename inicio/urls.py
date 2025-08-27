from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_sahumerio/<str:descripcion>/<int:precio>/', views.crear_sahumerio, name='crear_sahumerio'),
]

