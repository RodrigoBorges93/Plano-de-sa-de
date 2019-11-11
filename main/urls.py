from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^cadastro_usuario/', views.Criar_usuario.as_view(), name = 'cadastro'),
  path('', include('sendemail.urls')),

]
