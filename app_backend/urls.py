from django.urls import path
from app_backend import views

urlpatterns = [
    path('', views.homeView, name='backend-home' ),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.profileView, name='profile'),
]