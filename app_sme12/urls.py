from django.urls import path
from app_sme12 import views

urlpatterns = [
    path('dashboard-regis/', views.dashboardRegisView, name='dashboard-regis'),
    path('dashboard-score/', views.dashboardScoreView, name='dashboard-score'),

    path('sme-info/<int:compet_id>', views.smeInfo, name='sme-info'),

    path('register-list/', views.registerListView, name='register-list' ),
    path('screen-list/', views.screenListView, name='screen-list'),
    path('interview-list/', views.interviewListView, name='interview-list'),
    path('evaluate-list/', views.evaluateListView, name='evaluate-list'),
    path('candidate-list/', views.candidateListView, name='candidate-list'),
    
    path('register-form/', views.registerFormView, name='register-form'),
    path('sitevisite-form/<int:ent_id>/<int:comp_id>', views.sitevisiteFormView, name='sitevisite-form'),

    path('sitevisite-update/<int:sitevisit_id>', views.sitevisiteUpdate, name='sitevisite-update'),

    path('register-cancle/<int:compet_id>', views.cancleRegister, name='register-cancle'),

    path('ajax/load-amphur/', views.load_amphur, name='ajax_load_amphur'),
    path('ajax/load-tumbol/', views.load_tumbol, name='ajax_load_tumbol'),
    path('ajax/load-busgroup/', views.load_businessgroup, name='ajax_load_busgroup'), 
    path('ajax/load-employment/', views.load_employment, name='ajax_load_employment'), 
    path('ajax/load-revenue/', views.load_revenue, name='ajax_load_revenue'), 

]
