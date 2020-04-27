from django.urls import path
from app_sme12 import views

urlpatterns = [
    path('register-form/', views.registerFormView, name='register-form'),
    path('register-list/', views.registerListView, name='register-list' ),
    path('screen-list/', views.screenListView, name='screen-list'),
    path('interview-list/', views.interviewListView, name='interview-list'),
    path('evaluate-list/', views.evaluateListView, name='evaluate-list'),
    path('candidate-list/', views.candidateListView, name='candidate-list'),
    path('dashboard-sme/', views.dashboardView, name='dashboard-sme'),

    path('register-wizard/', views.registerTestView, name='register-wizard'),
]
