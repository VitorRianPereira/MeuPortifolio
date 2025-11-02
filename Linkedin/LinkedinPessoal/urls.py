from django.urls import path, include
from . import views

urlpatterns= [
      path('', views.contato, name='contato'),
      path('projeto/', views.projeto, name='projeto')
]