from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.index_view, name="home"),
    path('sobre/', views.sobre, name="sobre"),
    path('portifolio', views.portifolio, name="portifolio"),
    path('administracao/', views.administracao, name='administracao'),
    path('contato/', include('LinkedinPessoal.urls')),
]
