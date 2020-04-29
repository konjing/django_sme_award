from django.db import models
from app_backend.models import Enterpise, Competition
 

# Create your models here.
class FormRegister(models.Model):
    CHOICES = [
        (1, 'สนใจเข้ารับการฝึกอบรมและเข้าร่วมประกวดรางวัล'),
        (2, 'สนใจเฉพาะการเข้าร่วมประกวดรางวัล'),
        (3, 'สนใจเข้ารับการฝึกอบรม'),
    ]

    regis_code = models.CharField(verbose_name='รหัสสมัคร', max_length=20)
    regis_name = models.CharField(verbose_name='ผู้สมัคร', max_length=200, null=True, blank=True)
    regis_date = models.DateField(verbose_name='วันที่สมัคร', null=True, blank=True)
    
    employ = models.CharField(verbose_name='จำนวนการจ้างงาน', max_length=100, null=True, blank=True)
    revenue = models.CharField(verbose_name='รายได้ต่อปี', max_length=100, null=True, blank=True)
    
    profit = models.DecimalField(verbose_name='กำไร', max_digits=10, decimal_places=2, null=True, blank=True)
    
    news_from = models.CharField(verbose_name='รับข่าวสารจากช่องทาง', max_length=100, null=True, blank=True)
    news_from_etc = models.CharField(verbose_name='รับข่าวสารจากช่องทางอื่นๆ', max_length=100, null=True, blank=True)

    join_choice = models.PositiveSmallIntegerField(verbose_name='เลือกอบรมหรือประกวด', choices=CHOICES, default=2)
    training_course = models.CharField(verbose_name='หลักสูตรอบรม', max_length=100, null=True, blank=True)
    trainee1_name = models.CharField(verbose_name='ชื่อผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    trainee1_id_card = models.CharField(verbose_name='เลขบัตรประชาชนผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    trainee1_mobile = models.CharField(verbose_name='เบอร์มิอถือผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    trainee1_email = models.EmailField(verbose_name='อีเมลผู้เข้าอบรมคนที่1', null=True, blank=True)
    trainee2_name = models.CharField(verbose_name='ชื่อผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    trainee2_id_card = models.CharField(verbose_name='เลขบัตรประชาชนผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    trainee2_mobile = models.CharField(verbose_name='เบอร์มิอถือผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    trainee2_email = models.EmailField(verbose_name='อีเมลผู้เข้าอบรมคนที่2', null=True, blank=True)
    
    agreement = models.BooleanField(verbose_name='ยินยอมข้อตกลง', null=True, blank=True)
    tsic_no = models.CharField(verbose_name='เลข tsic', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.regis_code


class FormInterview(models.Model):
    interviewer = models.CharField(verbose_name='ผู้สัมภาษณ์', max_length=200)
    interview_at = models.DateField(verbose_name='วันที่', auto_now_add=True)

    def __str__(self):
        return self.interviewer


class FormSiteVisit(models.Model):
    visiter = models.CharField(verbose_name='ผู้ไปเยี่ยมชม', max_length=200)
    visit_at = models.DateField(verbose_name='วันที่', auto_now_add=True)

    def __str__(self):
        return self.visiter


class SmeCompetition(models.Model):
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
        (10, 'เข้าชิงรางวัล'),

    ]
    
    enterpise = models.ForeignKey(Enterpise, blank=True, null=True, on_delete=models.SET_NULL) 
    competition = models.ForeignKey(Competition, blank=True, null=True, on_delete=models.SET_NULL)
    state = models.PositiveSmallIntegerField(verbose_name='สถานะการประกวด', choices=STATE, default=1)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)
    form_register = models.OneToOneField(FormRegister, blank=True, null=True, on_delete=models.SET_NULL)
    form_interview = models.OneToOneField(FormInterview, blank=True, null=True, on_delete=models.SET_NULL)
    form_site_visit = models.OneToOneField(FormSiteVisit, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.enterpise.name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return '{} - {}'.format(self.enterpise.name, self.competition.name)      
        

