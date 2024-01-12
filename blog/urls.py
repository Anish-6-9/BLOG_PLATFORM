from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.log_in, name='log_in'),
    path('logout', views.log_out, name='log_out'),
    path('search', views.searchbar, name='search'),
    path('edit', views.edit, name='edit'),
]
