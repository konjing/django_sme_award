from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Q

from app_sme12.models import SmeCompetition


@login_required(login_url='login')
def reportListView(request):
    """ หน้าหลักรายงาน SME12 """

    context = {}
    return render(request, 'app_sme12/report/report_list.html', context)


# สรุปจำนวนผู้สมัคร --------------------------------------------------------------
@login_required(login_url='login')
def reportTotalReportView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัคร แต่ละขั้นตอน"""
    if by_step == 'regis':
        step_name = 'สมัคร'
        queryset = SmeCompetition.objects \
            .values('enterpise__business_group', 'enterpise__business_group__name', 'enterpise__business_type__name') \
            .annotate(toal_business_group=Count('enterpise__business_group', filter=Q(active=True))) \
            .order_by('enterpise__business_type__name')

        target = 1000
        total_register = SmeCompetition.objects.filter(active=True).count()
        percent_register = '{0:.2%}'.format(total_register/target)

        context = {'queryset': queryset, 'target': target, 'total_register': total_register,
               'percent_register': percent_register, 'step_name':step_name}
    elif by_step == 'screen':
        step_name = 'ตรวจประเมิน'
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
            .values('enterpise__business_group', 'enterpise__business_group__name', 'enterpise__business_type__name') \
            .annotate(toal_business_group=Count('enterpise__business_group', filter=Q(active=True))) \
            .order_by('enterpise__business_type__name')

        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        context = {'queryset': queryset, 'total_sme': total_sme, 'step_name':step_name}
    elif by_step == 'interview':
        step_name = 'สัมภาษณ์'
        queryset = SmeCompetition.objects.filter(state__in=[4,6,7,8,9,10,11]) \
            .values('enterpise__business_group', 'enterpise__business_group__name', 'enterpise__business_type__name') \
            .annotate(toal_business_group=Count('enterpise__business_group', filter=Q(active=True))) \
            .order_by('enterpise__business_type__name')

        total_sme = SmeCompetition.objects.filter(state__in=[4,6,7,8,9,10,11]).count()
        context = {'queryset': queryset, 'total_sme': total_sme, 'step_name':step_name}
    else:
        step_name = ' Site visit'
        queryset = SmeCompetition.objects.filter(state__in=[6,8,9,10,11]) \
            .values('enterpise__business_group', 'enterpise__business_group__name', 'enterpise__business_type__name') \
            .annotate(toal_business_group=Count('enterpise__business_group', filter=Q(active=True))) \
            .order_by('enterpise__business_type__name')

        total_sme = SmeCompetition.objects.filter(state__in=[6,8,9,10,11]).count()
        context = {'queryset': queryset, 'total_sme': total_sme, 'step_name':step_name}

    return render(request, 'app_sme12/report/total_report.html', context)

@login_required(login_url='login')
def reportTotalSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัคร ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__business_group', 'enterpise__business_group__name', 'enterpise__business_type__name') \
        .annotate(step_register=Count('enterpise__business_group')) \
        .annotate(step_screen=Count('enterpise__business_group', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__business_group', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_summary=Count('enterpise__business_group', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__business_type__name')    

    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/total_summary.html', context)

# สรุปจำนวนผู้สมัคร ตามจังหวัดที่ตั้งธุรกิจ ----------------------------------------------
@login_required(login_url='login')
def reportProvinceView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัครตามจังหวัดที่ตั้งธุรกิจ สมัครประกวด"""
    if by_step == 'regis':
        queryset = SmeCompetition.objects \
                .values('enterpise__province', 'enterpise__province__name') \
                .annotate(toal_province=Count('enterpise__province', filter=Q(active=True))) \
                .order_by('enterpise__province__name')
        total_sme = SmeCompetition.objects.filter(active=True).count()
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .values('enterpise__province', 'enterpise__province__name') \
                .annotate(toal_province=Count('enterpise__province', filter=Q(active=True))) \
                .order_by('enterpise__province__name')
        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .values('enterpise__province', 'enterpise__province__name') \
                .annotate(toal_province=Count('enterpise__province', filter=Q(active=True))) \
                .order_by('enterpise__province__name')
        total_sme = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]).count()
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .values('enterpise__province', 'enterpise__province__name') \
                .annotate(toal_province=Count('enterpise__province', filter=Q(active=True))) \
                .order_by('enterpise__province__name')
        total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
        step_name = ' Site visit'

    context = {'queryset':queryset, 'total_sme':total_sme, 'step_name':step_name}
    return render(request, 'app_sme12/report/province_report.html', context)

@login_required(login_url='login')
def reportProvinceSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัครตามจังหวัดที่ตั้งธุรกิจ ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__province', 'enterpise__province__name') \
        .annotate(step_register=Count('enterpise__province')) \
        .annotate(step_screen=Count('enterpise__province', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__province', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_sitevisit=Count('enterpise__province', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__province__name') 
    total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
    
    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/province_summary.html', context)

# สรุปจำนวนผู้สมัคร ตามสถานะธุรกิจ ----------------------------------------------
@login_required(login_url='login')
def reportBusinessModelView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัครตามสถานะธุรกิจ"""
    if by_step == 'regis':
        queryset = SmeCompetition.objects \
                .values('enterpise__business_model', 'enterpise__business_model__name') \
                .annotate(total_count=Count('enterpise__business_model')) \
                .order_by('enterpise__business_model__name')
        total_sme = SmeCompetition.objects.filter(active=True).count()
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .values('enterpise__business_model', 'enterpise__business_model__name') \
                .annotate(total_count=Count('enterpise__business_model')) \
                .order_by('enterpise__business_model__name')
        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .values('enterpise__business_model', 'enterpise__business_model__name') \
                .annotate(total_count=Count('enterpise__business_model')) \
                .order_by('enterpise__business_model__name')
        total_sme = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]).count()
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .values('enterpise__business_model', 'enterpise__business_model__name') \
                .annotate(total_count=Count('enterpise__business_model')) \
                .order_by('enterpise__business_model__name')
        total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
        step_name = ' Site visit'

    context = {'queryset':queryset, 'total_sme':total_sme, 'step_name':step_name}
    return render(request, 'app_sme12/report/businessmodel_report.html', context)

@login_required(login_url='login')
def reportBusniessModelSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัครตามสถานะธุรกิจ ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__business_model', 'enterpise__business_model__name') \
        .annotate(step_register=Count('enterpise__business_model')) \
        .annotate(step_screen=Count('enterpise__business_model', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__business_model', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_sitevisit=Count('enterpise__business_model', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__business_model__name') 
    total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
    
    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/businessmodel_summary.html', context)

# สรุปจำนวนผู้สมัคร ตามประเภทกิจการ ----------------------------------------------
@login_required(login_url='login')
def reportBusinessTypeView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัครตามประเภทกิจการ"""
    if by_step == 'regis':
        queryset = SmeCompetition.objects \
                .values('enterpise__business_type', 'enterpise__business_type__name') \
                .annotate(total_count=Count('enterpise__business_type')) \
                .order_by('enterpise__business_type__name')
        total_sme = SmeCompetition.objects.filter(active=True).count()
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .values('enterpise__business_type', 'enterpise__business_type__name') \
                .annotate(total_count=Count('enterpise__business_type')) \
                .order_by('enterpise__business_type__name')
        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .values('enterpise__business_type', 'enterpise__business_type__name') \
                .annotate(total_count=Count('enterpise__business_type')) \
                .order_by('enterpise__business_type__name')
        total_sme = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]).count()
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .values('enterpise__business_type', 'enterpise__business_type__name') \
                .annotate(total_count=Count('enterpise__business_type')) \
                .order_by('enterpise__business_type__name')
        total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
        step_name = ' Site visit'

    context = {'queryset':queryset, 'total_sme':total_sme, 'step_name':step_name}
    return render(request, 'app_sme12/report/businesstype_report.html', context)

@login_required(login_url='login')
def reportBusniessTypeSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัครตามประเภทกิจการ ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__business_type', 'enterpise__business_type__name') \
        .annotate(step_register=Count('enterpise__business_type')) \
        .annotate(step_screen=Count('enterpise__business_type', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__business_type', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_sitevisit=Count('enterpise__business_type', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__business_type__name') 
    total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
    
    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/businesstype_summary.html', context)

# สรุปจำนวนผู้สมัคร ตามกลุ่มธุรกิจ ----------------------------------------------
@login_required(login_url='login')
def reportBusinessGroupView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัครตามกลุ่มธุรกิจ"""
    if by_step == 'regis':
        queryset = SmeCompetition.objects \
                .values('enterpise__business_group', 'enterpise__business_group__name') \
                .annotate(total_count=Count('enterpise__business_group')) \
                .order_by('enterpise__business_group__name')
        total_sme = SmeCompetition.objects.filter(active=True).count()
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .values('enterpise__business_group', 'enterpise__business_group__name') \
                .annotate(total_count=Count('enterpise__business_group')) \
                .order_by('enterpise__business_group__name')
        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .values('enterpise__business_group', 'enterpise__business_group__name') \
                .annotate(total_count=Count('enterpise__business_group')) \
                .order_by('enterpise__business_group__name')
        total_sme = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]).count()
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .values('enterpise__business_group', 'enterpise__business_group__name') \
                .annotate(total_count=Count('enterpise__business_group')) \
                .order_by('enterpise__business_group__name')
        total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
        step_name = ' Site visit'

    context = {'queryset':queryset, 'total_sme':total_sme, 'step_name':step_name}
    return render(request, 'app_sme12/report/businessgroup_report.html', context)

@login_required(login_url='login')
def reportBusniessGroupSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัครตามกลุ่มธุรกิจ ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__business_group', 'enterpise__business_group__name') \
        .annotate(step_register=Count('enterpise__business_group')) \
        .annotate(step_screen=Count('enterpise__business_group', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__business_group', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_sitevisit=Count('enterpise__business_group', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__business_group__name') 
    total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
    
    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/businessgroup_summary.html', context)

# สรุปจำนวนผู้สมัครตาม TSIC ----------------------------------------------
@login_required(login_url='login')
def reportTsicView(request, by_step):
    """ รายงาน สรุปจำนวนผู้สมัครตาม TSIC"""
    if by_step == 'regis':
        queryset = SmeCompetition.objects \
                .values('enterpise__tsic_no') \
                .annotate(total_count=Count('enterpise__tsic_no')) \
                .order_by('enterpise__tsic_no')
        total_sme = SmeCompetition.objects.filter(active=True).count()
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .values('enterpise__tsic_no') \
                .annotate(total_count=Count('enterpise__tsic_no')) \
                .order_by('enterpise__tsic_no')
        total_sme = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]).count()
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .values('enterpise__tsic_no') \
                .annotate(total_count=Count('enterpise__tsic_no')) \
                .order_by('enterpise__tsic_no')
        total_sme = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]).count()
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .values('enterpise__tsic_no') \
                .annotate(total_count=Count('enterpise__tsic_no')) \
                .order_by('enterpise__tsic_no')
        total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
        step_name = ' Site visit'

    context = {'queryset':queryset, 'total_sme':total_sme, 'step_name':step_name}
    return render(request, 'app_sme12/report/tsic_report.html', context)

@login_required(login_url='login')
def reportTsicSummaryView(request):
    """ รายงาน สรุปจำนวนผู้สมัครตาม TSIC ทุกขั้นตอน"""
    queryset = SmeCompetition.objects \
        .values('enterpise__tsic_no') \
        .annotate(step_register=Count('enterpise__tsic_no')) \
        .annotate(step_screen=Count('enterpise__tsic_no', filter=Q(state__in=[2,4,5, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_interview=Count('enterpise__tsic_no', filter=Q(state__in=[4, 6, 7, 8, 9, 10, 11]))) \
        .annotate(step_sitevisit=Count('enterpise__tsic_no', filter=Q(state__in=[6, 8, 9, 10]))) \
        .order_by('enterpise__tsic_no') 
    total_sme = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]).count()
    
    total_register =  SmeCompetition.objects.filter(active=True).count()
    total_screen =  SmeCompetition.objects.filter(active=True, state__in=[2,4,5,6,7,8,9,10,11]).count()
    total_interview =  SmeCompetition.objects.filter(active=True, state__in=[4, 6, 7, 8, 9, 10, 11]).count()
    total_summary =  SmeCompetition.objects.filter(active=True, state__in=[6, 8, 9, 10, 11]).count()

    context = {'queryset': queryset, 'total_register':total_register, 'total_screen':total_screen \
                ,'total_interview':total_interview, 'total_summary':total_summary}
    return render(request, 'app_sme12/report/tsic_summary.html', context)


# รายชื่อผู้เข้าร่วมประกวด ----------------------------------------------
@login_required(login_url='login')
def reportSmeawardView(request, by_step):
    """ รายชื่อผู้เข้าร่วมประกวด """    
    if by_step == 'regis':
        queryset = SmeCompetition.objects.order_by('id')
        step_name = 'สมัคร'
    elif by_step == 'screen':
        queryset = SmeCompetition.objects.filter(state__in=[2,4,5,6,7,8,9,10,11]) \
                .order_by('id')
        step_name = 'ตรวจประเมิน'
    elif by_step == 'interview':
        queryset = SmeCompetition.objects.filter(state__in=[4, 6, 7, 8, 9, 10, 11]) \
                .order_by('id')
        step_name = 'สัมภาษณ์'
    else:
        queryset = SmeCompetition.objects.filter(state__in=[6, 8, 9, 10, 11]) \
                .order_by('id')
        step_name = ' Site visit'    

    context = {'queryset':queryset, 'step_name':step_name}
    return render(request, 'app_sme12/report/join_report.html', context)

