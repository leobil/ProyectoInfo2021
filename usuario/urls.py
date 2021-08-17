from django.urls import path
from usuario import views as usuario_views

urlpatterns = [
    path('registro/', usuario_views.registro),
    path('login/', usuario_views.login),
    path('logout/', usuario_views.logout),
    path('',usuario_views.home),
    ]