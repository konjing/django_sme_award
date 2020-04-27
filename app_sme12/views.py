from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from app_sme12.models import SmeCompetition, FormRegister
from app_backend.models import Owner, Enterpise, Competition

from app_sme12.forms import RegistrationForm

def dashboardView(request):

    context = {}
    return render(request, 'app_sme12/dashboard.html', context)

def registerTestView(request):
    form = RegistrationForm()

    context = {'form':form}
    return render(request, 'app_sme12/register_form_v1.html', context)

def registerFormView(request):
    """ แบบฟอร์มลงทะเบียน """
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            owner = Owner.objects.create(
                name = request.POST.get('own_name'),
                card_id = request.POST.get('own_card_id'),
            )

            enterpise = Enterpise.objects.create(
                name = request.POST.get('ent_name'),
                sme_code = request.POST.get('ent_sme_code'),  
                owner = owner,             
            )    

            form_register = FormRegister.objects.create(
                regis_code = request.POST.get('regis_code'),                              
            )

            sme_comp = SmeCompetition.objects.create(
                enterpise = enterpise,
                competition = Competition.objects.get(id=1),
                state = 1,
                form_register = form_register,
            )

            messages.success(request, 'ลงทะเบียนผู้สมัครสำเร็จ')        
            return redirect('register-form')

    context = {'form':form}
    return render(request, 'app_sme12/register_form.html', context)


def registerListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ส่งข้อมูลเข้ามา """
    queryset = SmeCompetition.objects.filter(state=1, competition=1)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            SmeCompetition.objects.filter(id=regis_id).update(state=2)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการตรวจสอบคุุณสมบัติ'.format(total_select))        
        return redirect('register-list')

    context = {'queryset':queryset}
    return render(request, 'app_sme12/register_list.html', context) 


def screenListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจสอบคุณสมบัติ """
    queryset = SmeCompetition.objects.filter(state=2, competition=1)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            SmeCompetition.objects.filter(id=regis_id).update(state=4)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการตรวจประเมินเบื้องต้น'.format(total_select))        
        return redirect('screen-list')

    context = {'queryset':queryset}
    return render(request, 'app_sme12/screen_list.html', context) 


def interviewListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจประเมินเบื้องต้น """
    queryset = SmeCompetition.objects.filter(state=4, competition=1)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            SmeCompetition.objects.filter(id=regis_id).update(state=6)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านการสัมภาษณ์เพื่อเลือกไป Site visit'.format(total_select))        
        return redirect('interview-list')

    context = {'queryset':queryset}
    return render(request, 'app_sme12/interview_list.html', context)


def evaluateListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการสัมภาษณ์เพื่อเลือกไป Site visit """
    queryset = SmeCompetition.objects.filter(state=6, competition=1)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            SmeCompetition.objects.filter(id=regis_id).update(state=8)

        messages.success(request, 'ผู้สมัคร {} ราย ผ่านเกณฑ์พิจารณาในแต่ละกลุ่ม'.format(total_select))        
        return redirect('evaluate-list')

    context = {'queryset':queryset}
    return render(request, 'app_sme12/evaluate_list.html', context)


def candidateListView(request):    
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านเข้าชิงรางวัลในแต่ละกลุ่ม """
    queryset = SmeCompetition.objects.filter(state=8, competition=1)

    if request.method == 'POST': #<- Checking for method type
        id_list = request.POST.getlist('regis_id')
        total_select = len(id_list)
        for regis_id in id_list:
            SmeCompetition.objects.filter(id=regis_id).update(state=10)

        messages.success(request, 'ผู้สมัคร {} ราย ได้รับรา่งวัล'.format(total_select))        
        return redirect('candidate-list')

    context = {'queryset':queryset}
    return render(request, 'app_sme12/candidate_list.html', context)
