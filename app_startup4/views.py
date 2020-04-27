from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from app_startup4.models import StartupCompetition


def registerListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ส่งข้อมูลเข้ามา """
    queryset = StartupCompetition.objects.filter(state=1, competition=2)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            StartupCompetition.objects.filter(id=regis_id).update(state=2)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการตรวจสอบคุุณสมบัติ'.format(total_select))        
        return redirect('st-register-list')

    context = {'queryset':queryset}
    return render(request, 'app_startup4/register_list.html', context) 


def screenListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจสอบคุณสมบัติ """
    queryset = StartupCompetition.objects.filter(state=2, competition=2)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            StartupCompetition.objects.filter(id=regis_id).update(state=4)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการตรวจประเมินเบื้องต้น'.format(total_select))        
        return redirect('st-screen-list')

    context = {'queryset':queryset}
    return render(request, 'app_startup4/screen_list.html', context) 


def interviewListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจประเมินเบื้องต้น """
    queryset = StartupCompetition.objects.filter(state=4, competition=2)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            StartupCompetition.objects.filter(id=regis_id).update(state=6)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการสัมภาษณ์เพื่อเลือกไป Site visit'.format(total_select))        
        return redirect('st-interview-list')

    context = {'queryset':queryset}
    return render(request, 'app_startup4/interview_list.html', context)


def evaluateListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการสัมภาษณ์เพื่อเลือกไป Site visit """
    queryset = StartupCompetition.objects.filter(state=6, competition=2)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            StartupCompetition.objects.filter(id=regis_id).update(state=8)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านเกณฑ์พิจารณาในแต่ละกลุ่ม'.format(total_select))        
        return redirect('st-evaluate-list')

    context = {'queryset':queryset}
    return render(request, 'app_startup4/evaluate_list.html', context)


def candidateListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านเข้าชิงรางวัลในแต่ละกลุ่ม """
    queryset = StartupCompetition.objects.filter(state=8, competition=2)

    # if request.method == 'POST': #<- Checking for method type
    #     id_list = request.POST.getlist('regis_id')
    #     total_select = len(id_list)
    #     for regis_id in id_list:
    #         StartupCompetition.objects.filter(id=regis_id).update(state=10)

    #     messages.success(request, 'ผู้สมัคร {} ราย ได้รับรา่งวัล'.format(total_select))        
    #     return redirect('st-candidate-list')

    context = {'queryset':queryset}
    return render(request, 'app_startup4/candidate_list.html', context)

