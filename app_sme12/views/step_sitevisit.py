from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from app_sme12.models import SmeCompetition, FormSiteVisit
from app_backend.models import Enterpise, Competition

from app_sme12.forms import SitevisitForm
import sweetify

# Form View ---------------------------------------------------------------
@login_required(login_url='login')
def sitevisiteFormView(request, ent_id, comp_id):
    """ ฟอร็มให้คะแนน Site visit """
    form = SitevisitForm()
    ent_obj = get_object_or_404(Enterpise, pk=ent_id)

    if request.method == 'POST':
        form = SitevisitForm(request.POST)
        if form.is_valid:
            site_score1 = int(request.POST.get('site_score1'))
            site_score2 = int(request.POST.get('site_score2'))
            site_score3 = int(request.POST.get('site_score3'))
            site_score4 = int(request.POST.get('site_score4'))
            site_score5 = int(request.POST.get('site_score5'))
            site_score6 = int(request.POST.get('site_score6'))
            site_score7 = int(request.POST.get('site_score7'))
            if site_score1 < 60 or site_score2 < 60 or site_score3 < 60 or site_score4 < 50 or site_score5 < 70 or site_score6 < 80 or site_score7 < 120:
                visit_summary = False
            else:
                visit_summary = True

            form_sitevisit = FormSiteVisit.objects.create(
                enterpise=ent_obj,
                site_score1=site_score1,
                site_score2=site_score2,
                site_score3=site_score3,
                site_score4=site_score4,
                site_score5=site_score5,
                site_score6=site_score6,
                site_score7=site_score7,
                visit_summary=visit_summary,
            )

            sme_competition = get_object_or_404(SmeCompetition, pk=comp_id)
            sme_competition.form_site_visit = form_sitevisit
            sme_competition.save()

            sweetify.success(
                request, 'ให้คะแนน {} เสร็จสิ้น'.format(ent_obj.name))
            # messages.success(request, 'ให้คะแนน {} เสร็จสิ้น'.format(ent_obj.name))

        return redirect('evaluate-list')

    context = {'form': form, 'ent_obj': ent_obj}
    return render(request, 'app_sme12/evaluate_form.html', context)

@login_required(login_url='login')
def sitevisiteUpdate(request, sitevisit_id):
    """ Update View """
    sitevisit = get_object_or_404(FormSiteVisit, pk=sitevisit_id)
    form = SitevisitForm(None, instance=sitevisit)
    if request.method == 'POST':
        form = SitevisitForm(request.POST)
        if form.is_valid:
            site_score1 = int(request.POST.get('site_score1'))
            site_score2 = int(request.POST.get('site_score2'))
            site_score3 = int(request.POST.get('site_score3'))
            site_score4 = int(request.POST.get('site_score4'))
            site_score5 = int(request.POST.get('site_score5'))
            site_score6 = int(request.POST.get('site_score6'))
            site_score7 = int(request.POST.get('site_score7'))
            if site_score1 < 60 or site_score2 < 60 or site_score3 < 60 or site_score4 < 50 or site_score5 < 70 or site_score6 < 80 or site_score7 < 120:
                visit_summary = False
            else:
                visit_summary = True

            sitevisit.site_score1 = site_score1
            sitevisit.site_score2 = site_score2
            sitevisit.site_score3 = site_score3
            sitevisit.site_score4 = site_score4
            sitevisit.site_score5 = site_score5
            sitevisit.site_score6 = site_score6
            sitevisit.site_score7 = site_score7
            sitevisit.visit_summary = visit_summary
            sitevisit.save()

            sweetify.success(
                request, 'แก้ไขคะแนน {} เสร็จสิ้น'.format(sitevisit.enterpise))
            # messages.success(request, 'แก้ไขคะแนน {} เสร็จสิ้น'.format(sitevisit.enterpise))

        return redirect('evaluate-list')

    context = {'form': form, 'sitevisit': sitevisit}
    return render(request, 'app_sme12/evaluate_form_update.html', context)

@login_required(login_url='login')
def evaluateListView(request):
    """ จัดการข้อมูลและพิจารณา ผู้สมัครที่ผ่านการสัมภาษณ์เพื่อเลือกไป Site visit """
    queryset = SmeCompetition.objects.filter(
        state=6, competition=1, active=True)
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
                SmeCompetition.objects.filter(id=regis_id).update(state=8)

            sweetify.success(
                request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
            # messages.success(request, 'ผู้สมัครผ่าน {} ราย '.format(total_select))
        else:
            id_list = request.POST.getlist('regis_id')
            total_select = len(id_list)
            for regis_id in id_list:
                SmeCompetition.objects.filter(id=regis_id).update(state=9)
            messages.warning(
                request, 'ผู้สมัครไม่ผ่าน {} ราย '.format(total_select))
        return redirect('evaluate-list')

    context = {'queryset': queryset, 'total_bus': total_bus, 'bus_type_production': bus_type_production,
               'bus_type_service': bus_type_service, 'bus_type_farm': bus_type_farm}
    return render(request, 'app_sme12/evaluate_list.html', context)