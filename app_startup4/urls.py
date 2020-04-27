from django.urls import path
from app_startup4 import views

urlpatterns = [
    path('st-register-list/', views.registerListView, name='st-register-list' ),
    path('st-screen-list/', views.screenListView, name='st-screen-list'),
    path('st-interview-list/', views.interviewListView, name='st-interview-list'),
    path('st-evaluate-list/', views.evaluateListView, name='st-evaluate-list'),
    path('st-candidate-list/', views.candidateListView, name='st-candidate-list'),

]
