from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Q

from app_sme12.models import SmeCompetition

@login_required(login_url='login')
def exportListView(request):
    """ หน้าหลัก Export ข้อมูล SME12 """

    context = {}
    return render(request, 'app_sme12/export/export_list.html', context)