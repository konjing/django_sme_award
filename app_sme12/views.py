from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from app_sme12.models import SmeCompetition, FormRegister
from app_backend.models import Owner, Enterpise, Competition, BusinessGroup, BusinessModel, BusinessType, Province, Amphur, Tumbol

from app_sme12.forms import RegistrationForm, Employment, Revenue, AuthorizeCapital, ProfitPrevious, Promote

def dashboardView(request):

    context = {}
    return render(request, 'app_sme12/dashboard.html', context)


def registerFormView(request):
    """ แบบฟอร์มลงทะเบียน """
    form = RegistrationForm()
    business_model = BusinessModel.objects.all().order_by('model_group')
    init_amphur = Amphur.objects.all()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)       
        if request.POST.get('f_employment_etc'):
            new_emp_etc = int(request.POST.get('f_employment_etc'))
        else:
            new_emp_etc = 0

        if request.POST.get('f_revenue_etc'):
            new_rev_etc = int(request.POST.get('f_revenue_etc').replace(',', ''))
        else:
            new_rev_etc = 0

        if form.is_valid():
            """ บันทึกข้อมูลลงตาราง  Owner """
            owner = Owner.objects.create(
                name = request.POST.get('owner_name'),
                card_id = request.POST.get('owner_card_id'),
                address_no = request.POST.get('owner_address_no'),
                mu = request.POST.get('owner_mu'), 
                soi = request.POST.get('owner_soi'),
                street = request.POST.get('owner_street'),
                province = Province.objects.get(pk=int(request.POST.get('owner_province'))),
                amphur = Amphur.objects.get(pk=int(request.POST.get('owner_amphur'))),
                postcode = request.POST.get('owner_postcode'),
                tel = request.POST.get('owner_tel'),
                fax = request.POST.get('owner_fax'),
                mobile = request.POST.get('owner_mobile'),
                email = request.POST.get('owner_email'),
            )

            """ บันทึกข้อมูลลงตาราง  Enterpise """
            enterpise = Enterpise.objects.create(
                name = request.POST.get('ent_name'),
                establish_date = request.POST.get('ent_establish_date'),
                sme_code = request.POST.get('ent_sme_code'),  
                sme_connext_code = request.POST.get('ent_sme_connext_code'),
                address_no = request.POST.get('ent_address_no'),
                mu = request.POST.get('ent_mu'),
                soi = request.POST.get('ent_soi'),
                street = request.POST.get('ent_street'),
                province = Province.objects.get(pk= int(request.POST.get('ent_province'))),
                amphur = Amphur.objects.get(pk=int(request.POST.get('ent_amphur'))),
                postcode = request.POST.get('ent_postcode'),
                tel = request.POST.get('ent_tel'),
                fax = request.POST.get('ent_fax'),
                email = request.POST.get('ent_email'),
                website = request.POST.get('ent_website'),

                owner = owner,  

                business_model = BusinessModel.objects.get(pk=int(request.POST.get('business_model'))),
                bus_model_etc1 = request.POST.get('bus_model_etc1'),
                bus_model_etc2 = request.POST.get('bus_model_etc2'),
                juristic_id = request.POST.get('juristic_id'),
                card_id = request.POST.get('card_id'),
                commercial_regis_number = request.POST.get('commercial_regis_number'),
                regis_number = request.POST.get('regis_number'),

                contact_name = request.POST.get('contact_name'), 
                contact_position = request.POST.get('contact_position'),
                contact_tel = request.POST.get('contact_tel'),
                contact_email = request.POST.get('contact_email'),

                business_type = BusinessType.objects.get(pk=int(request.POST.get('business_type'))),
                business_group = BusinessGroup.objects.get(pk=int(request.POST.get('business_group'))),
                # business_group_etc = request.POST.get('business_group_etc'),
                product_info = request.POST.get('product_info'),
                material = request.POST.get('material'),
                otop = request.POST.get('otop'),
            )    
                       
            """ บันทึกข้อมูลลงตาราง  FormRegister """
            form_register = FormRegister.objects.create(
                regis_code = request.POST.get('regis_code'),  
                employment = Employment.objects.get(id=int(request.POST.get('f_employment'))), 
                employment_etc = new_emp_etc, 
                revenue = Revenue.objects.get(id=int(request.POST.get('f_revenue'))), 
                revenue_etc = new_rev_etc, 
               
                authorize_capital = AuthorizeCapital.objects.get(id= int(request.POST.get('f_cap'))),
                profit_previous = ProfitPrevious.objects.get(id= int(request.POST.get('f_profit'))),

                promote_etc = request.POST.get('f_promote_etc'),
                
                # join_choice = request.POST.get('f_join_choice'),
                # training_course = request.POST.get('f_training_course'),
                # trainee1_name = request.POST.get('f_trainee1_name'),
                # trainee1_id_card = request.POST.get('f_trainee1_id_card'),
                # trainee1_mobile = request.POST.get('f_trainee1_mobile'),
                # trainee1_email = request.POST.get('f_trainee1_email'),
                # trainee2_name = request.POST.get('f_trainee2_name'),
                # trainee2_id_card = request.POST.get('f_trainee2_id_card'),
                # trainee2_mobile = request.POST.get('f_trainee2_mobile'),
                # trainee2_email = request.POST.get('f_trainee2_email'),
            )

            """ บันทึกข้อมูลลงตาราง  SmeCompetition """
            sme_comp = SmeCompetition.objects.create(
                enterpise = enterpise,
                competition = Competition.objects.get(id=1),
                state = 1,
                form_register = form_register,
            )

            if request.POST.get('ent_tumbol'):
                """ บันทึกตำบลลงตาราง กรณีที่กรอกตำบล(สถานประกอบการ)"""
                ent_tumbol_id = int(request.POST.get('ent_tumbol'))
                enterpise.tumbol = Tumbol.objects.get(pk=ent_tumbol_id)
                enterpise.save()

            if request.POST.get('owner_tumbol'):
                """ บันทึกตำบลลงตาราง กรณีที่กรอกตำบล(เจ้าของ) """
                owner_tumbol_id = int(request.POST.get('owner_tumbol'))
                owner.tumbol = Tumbol.objects.get(pk=owner_tumbol_id)
                owner.save()

            for f_pro in request.POST.get('f_promote'):
                """ บันทึก รับข่าวสารจากช่องทางลงตาราง  M2M"""
                promote_obj =Promote.objects.get(id=int(f_pro))
                form_register.promote.add(promote_obj) 
            

            messages.success(request, 'ลงทะเบียนผู้สมัครสำเร็จ')        
            return redirect('register-list')
        # else:
        #     return HttpResponse('Form Invalid')

    context = {'form':form, 'business_model':business_model, 'init_amphur':init_amphur}
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


# ----------------- Helper ---------------------------------------------------
def load_amphur(request):
    """ Amphur Dependent/Chained Dropdown List """
    province_id = request.GET.get('province')
    amphur_list = Amphur.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'app_sme12/form_partial/amphur_dropdown_list_options.html', {'amphur_list': amphur_list})

def load_tumbol(request):
    """ Tumbol Dependent/Chained Dropdown List """
    amphur_id = request.GET.get('amphur')
    tumbol_list = Tumbol.objects.filter(amphur_id=amphur_id).order_by('name')
    return render(request, 'app_sme12/form_partial/tumbol_dropdown_list_options.html', {'tumbol_list': tumbol_list})

def load_businessgroup(request):
    """ Business Group Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    business_group_list = BusinessGroup.objects.filter(business_type_id=business_type_id).order_by('name')

    context = {'business_group_list':business_group_list}
    return render(request, 'app_sme12/form_partial/bus_group_dropdown_list_options.html', context)

def load_employment(request):
    """ Employment Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    employment_list = Employment.objects.filter(business_type_id=business_type_id).order_by('code')

    context = {'employment_list':employment_list}
    return render(request, 'app_sme12/form_partial/employment_dropdown_list_options.html', context)

def load_revenue(request):
    """ Revenue Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    revenue_list = Revenue.objects.filter(business_type_id=business_type_id).order_by('code')

    context = {'revenue_list':revenue_list}
    return render(request, 'app_sme12/form_partial/revenue_dropdown_list_options.html', context)
