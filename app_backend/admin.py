from django.contrib import admin
from app_backend.models import *
from app_sme12.models import *
from app_startup4.models import *

# app_backend models here.
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(Amphur)
admin.site.register(Tumbol)
admin.site.register(Enterpise)
admin.site.register(Owner)
admin.site.register(BusinessGroup)
admin.site.register(BusinessModel)
admin.site.register(BusinessType)
admin.site.register(Competition)

# app_sme12 models here.
admin.site.register(SmeCompetition)
admin.site.register(FormRegister)
admin.site.register(FormInterview)
admin.site.register(FormSiteVisit)
admin.site.register(Employment)
admin.site.register(Revenue)
admin.site.register(AuthorizeCapital)
admin.site.register(ProfitPrevious)
admin.site.register(Promote)
admin.site.register(RegisChoice)
admin.site.register(Course)


# app_startup4 models here.
admin.site.register(StartupCompetition)
admin.site.register(FormRegisterStartup)
admin.site.register(FormInterviewStartup)

