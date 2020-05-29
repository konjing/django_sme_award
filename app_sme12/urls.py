from django.urls import path
from app_sme12.views import views
from app_sme12.views import report
from app_sme12.views import export
from app_sme12.views import step_regis
from app_sme12.views import step_sitevisit


urlpatterns = [
    path('dashboard-regis/', views.dashboardRegisView, name='dashboard-regis'),
    path('dashboard-score/', views.dashboardScoreView, name='dashboard-score'),
    path('dashboard-final/', views.dashboardFinalView, name='dashboard-final'),

    path('sme-info/<int:compet_id>', views.smeInfo, name='sme-info'),

    path('register-form/', step_regis.registerFormView, name='register-form'),
    path('register-list/', step_regis.registerListView, name='register-list' ),
    path('register-cancle/<int:compet_id>', step_regis.cancleRegister, name='register-cancle'),

    path('sitevisite-form/<int:ent_id>/<int:comp_id>', step_sitevisit.sitevisiteFormView, name='sitevisite-form'),
    path('sitevisite-update/<int:sitevisit_id>', step_sitevisit.sitevisiteUpdate, name='sitevisite-update'),
    path('evaluate-list/', step_sitevisit.evaluateListView, name='evaluate-list'),
    
    path('interview-list/', views.interviewListView, name='interview-list'),
    path('interview-form/<int:ent_id>/<int:comp_id>', views.interviewFormView, name='interview-form'),
    path('interview-update/<int:interview_id>', views.interviewUpdate, name='interview-update'),

    path('candidate-list/', views.candidateListView, name='candidate-list'),
    path('screen-list/', views.screenListView, name='screen-list'),

    path('ajax/load-amphur/', views.load_amphur, name='ajax_load_amphur'),
    path('ajax/load-tumbol/', views.load_tumbol, name='ajax_load_tumbol'),
    path('ajax/load-busgroup/', views.load_businessgroup, name='ajax_load_busgroup'), 
    path('ajax/load-employment/', views.load_employment, name='ajax_load_employment'), 
    path('ajax/load-revenue/', views.load_revenue, name='ajax_load_revenue'), 

    path('report-list/', report.reportListView, name='report-list'),    
    path('total-report/<str:by_step>', report.reportTotalReportView, name='total-report'),
    path('total-summary/', report.reportTotalSummaryView, name='total-summary'),
    path('province-report/<str:by_step>', report.reportProvinceView, name='province-report'),
    path('province-summary/', report.reportProvinceSummaryView, name='province-summary'),
    path('businessmodel-report/<str:by_step>', report.reportBusinessModelView, name='businessmodel-report'),
    path('businessmodel-summary/', report.reportBusniessModelSummaryView, name='businessmodel-summary'),
    path('businesstype-report/<str:by_step>', report.reportBusinessTypeView, name='businesstype-report'),
    path('businesstype-summary/', report.reportBusniessTypeSummaryView, name='businesstype-summary'),
    path('businessgroup-report/<str:by_step>', report.reportBusinessGroupView, name='businessgroup-report'),
    path('businessgroup-summary/', report.reportBusniessGroupSummaryView, name='businessgroup-summary'),
    path('tsic-report/<str:by_step>', report.reportTsicView, name='tsic-report'),
    path('tsic-summary/', report.reportTsicSummaryView, name='tsic-summary'),
    path('smeaward-report/<str:by_step>', report.reportSmeawardView, name='smeaward-report'),

    path('export-list/', export.exportListView, name='export-list'),    


]
