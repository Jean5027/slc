from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("lista", views.cadastrar_lista, name="lista"),
    path("apaga_lista", views.apaga_lista ,name="apaga_lista"),

]
