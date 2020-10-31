from django.urls import path

from . import views 

urlpatterns = [
	 path('', views.Project1, name='Project1'),
	 path('register/', views.Registration, name='Registration'),
	 path('login/', views.Login, name='Login'),
	 path('dashboard/', views.Dashboard, name='Dashboard')
]