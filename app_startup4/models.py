from django.db import models
from app_backend.models import Enterpise, Competition


# Create your models here.
class FormRegisterStartup(models.Model):
    regis_name = models.CharField(verbose_name='ผู้สมัคร', max_length=200)
    regis_at = models.DateField(verbose_name='วันที่สมัคร', auto_now_add=True)
    tsic_no = models.CharField(verbose_name='เลข tsic', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.regis_name


class FormInterviewStartup(models.Model):
    interviewer = models.CharField(verbose_name='ผู้สัมภาษณ์', max_length=200)
    interview_at = models.DateField(verbose_name='วันที่', auto_now_add=True)

    def __str__(self):
        return self.interviewer


class StartupCompetition(models.Model):
    STATE = [
        (1, 'รอตรวจคุณสมบัติ'),
        (2, 'ผ่านตรวจคุณสมบัติ'),
        (3, 'ไม่ผ่านตรวจคุณสมบัติ'),
        (4, 'ผ่านตรวจประเมิน'),
        (5, 'ไม่ผ่านตรวจประเมิน'),
        (6, 'ผ่านสัมภาษณ์'),
        (7, 'ไม่ผ่านสัมภาษณ์'),
        (8, 'ผ่านการพิจารณา'),
        (9, 'ไม่ผ่านการพิจารณา'),
        
    ]

    enterpise = models.ForeignKey(Enterpise, null=True, on_delete=models.SET_NULL) 
    competition = models.ForeignKey(Competition, null=True, on_delete=models.SET_NULL)
    state = models.PositiveSmallIntegerField(verbose_name='สถานะการประกวด', choices=STATE, default=1)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)
    form_register = models.OneToOneField(FormRegisterStartup, blank=True, null=True, on_delete=models.SET_NULL)
    form_interview = models.OneToOneField(FormInterviewStartup, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return '{} {}'.format(self.enterpise, self.state)



