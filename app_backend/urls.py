from django.urls import path
from app_backend import views

urlpatterns = [
    path('', views.homeView, name='backend-home' ),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    path('enterpise-list/', views.enterpiseListView, name='enterpise-list'),
    path('enterpise-detail/<int:ent_id>', views.enterpiseDetailView, name='enterpise-detail'),

]