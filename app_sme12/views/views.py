from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from app_sme12.models import SmeCompetition, FormRegister, FormSiteVisit, FormInterview, Employment, Revenue, AuthorizeCapital, ProfitPrevious, Promote
from app_backend.models import Owner, Enterpise, Competition, BusinessGroup, BusinessModel, BusinessType, Province, Amphur, Tumbol

from app_sme12.forms import RegistrationForm, SitevisitForm, InterviewForm
import sweetify


# Form View ---------------------------------------------------------------
@login_required(login_url='login')
def interviewFormView(request, ent_id, comp_id):
    """ ฟอร็มให้คะแนน สัมภาษณ์ """
    form = InterviewForm()
    ent_obj = get_object_or_404(Enterpise, pk=ent_id)

    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid:
            score1 = int(request.POST.get('score1'))
            score2 = int(request.POST.get('score2'))
            score3 = int(request.POST.get('score3'))
            score4 = int(request.POST.get('score4'))
            score5 = int(request.POST.get('score5'))
            score6 = int(request.POST.get('score6'))
            score7 = int(request.POST.get('score7'))
            if score1 < 60 or score2 < 60 or score3 < 60 or score4 < 50 or score5 < 70 or score6 < 80 or score7 < 120:
                visit_summary = False
            else:
                visit_summary = True

            form_interview = FormInterview.objects.create(
                enterpise=ent_obj,
                score1=score1,
                score2=score2,
                score3=score3,
                score4=score4,
                score5=score5,
                score6=score6,
                score7=score7,
                visit_summary=visit_summary,
            )

            sme_competition = get_object_or_404(SmeCompetition, pk=comp_id)
            sme_competition.form_interview = form_interview
            sme_competition.save()

            sweetify.success(
                request, 'ให้คะแนน {} เสร็จสิ้น'.format(ent_obj.name))
            # messages.success(request, 'ให้คะแนน {} เสร็จสิ้น'.format(ent_obj.name))

        return redirect('interview-list')

    context = {'form': form, 'ent_obj': ent_obj}
    return render(request, 'app_sme12/interview_form.html', context)

# Update View ---------------------------------------------------------------
@login_required(login_url='login')
def interviewUpdate(request, interview_id):
    interview = get_object_or_404(FormInterview, pk=interview_id)
    form = InterviewForm(None, instance=interview)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid:
            score1 = int(request.POST.get('score1'))
            score2 = int(request.POST.get('score2'))
            score3 = int(request.POST.get('score3'))
            score4 = int(request.POST.get('score4'))
            score5 = int(request.POST.get('score5'))
            score6 = int(request.POST.get('score6'))
            score7 = int(request.POST.get('score7'))
            if score1 < 60 or score2 < 60 or score3 < 60 or score4 < 50 or score5 < 70 or score6 < 80 or score7 < 120:
                visit_summary = False
            else:
                visit_summary = True

            interview.score1 = score1
            interview.score2 = score2
            interview.score3 = score3
            interview.score4 = score4
            interview.score5 = score5
            interview.score6 = score6
            interview.score7 = score7
            interview.visit_summary = visit_summary
            interview.save()

            sweetify.success(
                request, 'แก้ไขคะแนน {} เสร็จสิ้น'.format(interview.enterpise))
            # messages.success(request, 'แก้ไขคะแนน {} เสร็จสิ้น'.format(interview.enterpise))

        return redirect('interview-list')

    context = {'form': form, 'interview': interview}
    return render(request, 'app_sme12/interview_form_update.html', context)

# List View ---------------------------------------------------------------
@login_required(login_url='login')
def screenListView(request):
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจสอบคุณสมบัติ """
    queryset = SmeCompetition.objects.filter(
        state=2, competition=1, active=True)
    total_bus = queryset.count()
    bus_type_production = queryset.filter(enterpise__business_type=1).count()
    bus_type_service = queryset.filter(enterpise__business_type=2).count()
    bus_type_farm = queryset.filter(enterpise__business_type=3).count()

    if request.method == 'POST':
        """ อัพเดตสถานะการตรวจสอบตาม check list  """
        if request.POST.get('approval') == 'pass':
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=4)
            sweetify.success(
                request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
            # messages.success(request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
        else:
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=5)
            messages.warning(
                request, 'ผู้สมัครไม่ผ่าน {} ราย '.format(total_select))
        return redirect('screen-list')

    context = {'queryset': queryset, 'total_bus': total_bus, 'bus_type_production': bus_type_production,
               'bus_type_service': bus_type_service, 'bus_type_farm': bus_type_farm}
    return render(request, 'app_sme12/screen_list.html', context)


@login_required(login_url='login')
def interviewListView(request):
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการตรวจประเมินเบื้องต้น """
    queryset = SmeCompetition.objects.filter(
        state=4, competition=1, active=True)
    total_bus = queryset.count()
    bus_type_production = queryset.filter(enterpise__business_type=1).count()
    bus_type_service = queryset.filter(enterpise__business_type=2).count()
    bus_type_farm = queryset.filter(enterpise__business_type=3).count()

    if request.method == 'POST':  # <- Checking for method type
        """ อัพเดตสถานะการตรวจสอบตาม check list  """
        if request.POST.get('approval') == 'pass':
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=6)
            sweetify.success(
                request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
            # messages.success(request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
        else:
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=7)
            messages.warning(
                request, 'ผู้สมัครไม่ผ่าน {} ราย '.format(total_select))
        return redirect('interview-list')

    context = {'queryset': queryset, 'total_bus': total_bus, 'bus_type_production': bus_type_production,
               'bus_type_service': bus_type_service, 'bus_type_farm': bus_type_farm}
    return render(request, 'app_sme12/interview_list.html', context)

@login_required(login_url='login')
def candidateListView(request):
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านเข้าชิงรางวัลในแต่ละกลุ่ม """
    queryset = SmeCompetition.objects.filter(
        state=8, competition=1, active=True)
    total_bus = queryset.count()
    bus_type_production = queryset.filter(enterpise__business_type=1).count()
    bus_type_service = queryset.filter(enterpise__business_type=2).count()
    bus_type_farm = queryset.filter(enterpise__business_type=3).count()

    if request.method == 'POST':  # <- Checking for method type
        """ อัพเดตสถานะการตรวจสอบตาม check list  """
        if request.POST.get('approval') == 'pass':
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=10)
            messages.success(
                request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
        else:
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=11)
            messages.warning(
                request, 'ผู้สมัครไม่ผ่าน {} ราย '.format(total_select))
        return redirect('register-list')

    context = {'queryset': queryset, 'total_bus': total_bus, 'bus_type_production': bus_type_production,
               'bus_type_service': bus_type_service, 'bus_type_farm': bus_type_farm}
    return render(request, 'app_sme12/candidate_list.html', context)

# DashBoard View ---------------------------------------------------------------
@login_required(login_url='login')
def dashboardRegisView(request):

    context = {}
    return render(request, 'app_sme12/dashboard_regis.html', context)


@login_required(login_url='login')
def dashboardScoreView(request):

    context = {}
    return render(request, 'app_sme12/dashboard_score.html', context)


@login_required(login_url='login')
def dashboardFinalView(request):
    """ DashBoard Final """
    register_info_box = SmeCompetition.objects.values('enterpise__business_type', 'enterpise__business_type__name').annotate(
        toal_business_type=Count('enterpise__business_type')).order_by('enterpise__business_type')
    register_info = {'bus_type1': register_info_box[0]['toal_business_type'], 'bus_type2': register_info_box[1]
                     ['toal_business_type'], 'bus_type3': register_info_box[2]['toal_business_type'], 'bus_total': register_info_box[0]['toal_business_type']+register_info_box[1]['toal_business_type']+register_info_box[2]['toal_business_type']}

    sme_rank = FormSiteVisit.objects.all().order_by('-score_total')

    context = {'register_info': register_info, 'sme_rank':sme_rank}
    return render(request, 'app_sme12/dashboard_final.html', context)


# SME info ----------------------------------------------------------------\
def smeInfo(request, compet_id):
    query_obj = get_object_or_404(SmeCompetition, pk=compet_id)
    str_bus_type = str(query_obj.enterpise.business_type)
    str_website = str(query_obj.enterpise.website)

    if query_obj.form_site_visit:
        percent_score1 = format(query_obj.form_site_visit.site_score1/120,
                                '.0%') if query_obj.form_site_visit.site_score1 is not None else 0
        percent_score2 = format(query_obj.form_site_visit.site_score2/120,
                                '.0%') if query_obj.form_site_visit.site_score2 is not None else 0
        percent_score3 = format(query_obj.form_site_visit.site_score3/120,
                                '.0%') if query_obj.form_site_visit.site_score3 is not None else 0
        percent_score4 = format(query_obj.form_site_visit.site_score4/100,
                                '.0%') if query_obj.form_site_visit.site_score4 is not None else 0
        percent_score5 = format(query_obj.form_site_visit.site_score5/140,
                                '.0%') if query_obj.form_site_visit.site_score5 is not None else 0
        percent_score6 = format(query_obj.form_site_visit.site_score6/160,
                                '.0%') if query_obj.form_site_visit.site_score6 is not None else 0
        percent_score7 = format(query_obj.form_site_visit.site_score7/240,
                                '.0%') if query_obj.form_site_visit.site_score7 is not None else 0
        total_score = query_obj.form_site_visit.site_score1 + query_obj.form_site_visit.site_score2 \
            + query_obj.form_site_visit.site_score3 + query_obj.form_site_visit.site_score4 \
            + query_obj.form_site_visit.site_score5 + query_obj.form_site_visit.site_score6 \
            + query_obj.form_site_visit.site_score7
        context = {'query_obj': query_obj, 'str_bus_type': str_bus_type, 'str_website': str_website,
                   'percent_score1': percent_score1, 'percent_score2': percent_score2,
                   'percent_score3': percent_score3, 'percent_score4': percent_score4,
                   'percent_score5': percent_score5, 'percent_score6': percent_score6,
                   'percent_score7': percent_score7, 'total_score': total_score
                   }
        return render(request, 'app_sme12/sme_info.html', context)

    context = {'query_obj': query_obj,
               'str_bus_type': str_bus_type, 'str_website': str_website}
    return render(request, 'app_sme12/sme_info.html', context)


# ----------------- Helper ---------------------------------------------------
def load_amphur(request):
    """ Amphur Dependent/Chained Dropdown List """
    province_id = request.GET.get('province')
    amphur_list = Amphur.objects.filter(
        province_id=province_id).order_by('name')
    return render(request, 'app_sme12/form_partial/amphur_dropdown_list_options.html', {'amphur_list': amphur_list})


def load_tumbol(request):
    """ Tumbol Dependent/Chained Dropdown List """
    amphur_id = request.GET.get('amphur')
    tumbol_list = Tumbol.objects.filter(amphur_id=amphur_id).order_by('name')
    return render(request, 'app_sme12/form_partial/tumbol_dropdown_list_options.html', {'tumbol_list': tumbol_list})


def load_businessgroup(request):
    """ Business Group Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    business_group_list = BusinessGroup.objects.filter(
        business_type_id=business_type_id).order_by('name')

    context = {'business_group_list': business_group_list}
    return render(request, 'app_sme12/form_partial/bus_group_dropdown_list_options.html', context)


def load_employment(request):
    """ Employment Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    employment_list = Employment.objects.filter(
        business_type_id=business_type_id).order_by('code')

    context = {'employment_list': employment_list}
    return render(request, 'app_sme12/form_partial/employment_dropdown_list_options.html', context)


def load_revenue(request):
    """ Revenue Dependent/Chained Dropdown List """
    business_type_id = request.GET.get('business_type')
    revenue_list = Revenue.objects.filter(
        business_type_id=business_type_id).order_by('code')

    context = {'revenue_list': revenue_list}
    return render(request, 'app_sme12/form_partial/revenue_dropdown_list_options.html', context)
