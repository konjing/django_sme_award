from django.db import models
from django.core import validators
from app_backend.models import Enterpise, Competition, BusinessType


# Create your models here.
class Employment(models.Model):
    """ LT ตัวเลือกการจ้างงาน """
    business_type = models.ForeignKey(BusinessType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name='จำนวนการจ้างงาน', max_length=100, null=True, blank=True)
    short_name = models.CharField(verbose_name='จำนวนการจ้างงาน(ย่อ)', max_length=50, null=True, blank=True)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        # return '{} - {}'.format(self.business_type.name, self.name)
        return '{}'.format(self.name)


class Revenue(models.Model):
    """ LT ตัวเลือกรายได้ต่อปี """
    business_type = models.ForeignKey(BusinessType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name='รายได้ต่อปี', max_length=100, null=True, blank=True)
    short_name = models.CharField(verbose_name='รายได้ต่อปี(ย่อ)', max_length=50, null=True, blank=True)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        # return '{} - {}'.format(self.code, self.name)
        return '{}'.format(self.name)


class AuthorizeCapital(models.Model):
    """ LT ตัวเลือกทุนจดทะเบียน """
    name = models.CharField(verbose_name='ทุนจดทะเบียน', max_length=100)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        return self.name


class ProfitPrevious(models.Model):
    """ LT ตัวเลือกกำไร (ณ สิ้นปีก่อนหน้า) """
    name = models.CharField(verbose_name='กำไร', max_length=100)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        return self.name


class Promote(models.Model):
    """ LT(Many to Many) ช่องทางการรับข่าวสาร """
    name = models.CharField(verbose_name='ช่องทาง', max_length=100)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        return self.name


class RegisChoice(models.Model):
    """ LT ตัวเลือกประกวดและอบรม """
    name = models.CharField(verbose_name='ตัวเลือก', max_length=100)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    """ LT หลักสูตรที่อบรม """
    name = models.CharField(verbose_name='หลักสูตร', max_length=100)
    code = models.CharField(verbose_name='รหัส', max_length=20, null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะการใช้งาน', default=True)

    def __str__(self):
        return self.name

class FormRegister(models.Model):
    """ ฟอร์มลงทะเบียน """
    REGIS_CHOICES = [
        (1, 'สนใจเข้ารับการฝึกอบรมและเข้าร่วมประกวดรางวัล'),
        (2, 'สนใจเฉพาะการเข้าร่วมประกวดรางวัล'),
        (3, 'สนใจเข้ารับการฝึกอบรม'),
    ]

    regis_code = models.CharField(verbose_name='รหัสสมัคร', max_length=20)
    regis_name = models.CharField(verbose_name='ผู้สมัคร', max_length=200, null=True, blank=True)
    regis_date = models.DateField(verbose_name='วันที่สมัคร', null=True, blank=True)
    
    employment = models.ForeignKey(Employment, null=True, blank=True, on_delete=models.SET_NULL)
    employment_etc = models.IntegerField(verbose_name='จำนวนจ้างสำหรับธุรกิจเกษตร', null=True, blank=True)
    revenue = models.ForeignKey(Revenue, null=True, blank=True, on_delete=models.SET_NULL)
    revenue_etc = models.IntegerField(verbose_name='รายได้สำหรับธุรกิจเกษตร', null=True, blank=True)
    
    authorize_capital = models.ForeignKey(AuthorizeCapital, null=True, blank=True, on_delete=models.SET_NULL)
    profit_previous = models.ForeignKey(ProfitPrevious, null=True, blank=True, on_delete=models.SET_NULL)
    
    promote = models.ManyToManyField(Promote)
    promote_etc = models.CharField(verbose_name='รับข่าวสารจากช่องทางอื่นๆ', max_length=100, null=True, blank=True)


    # regis_choice = models.ForeignKey(RegisChoice, null=True, blank=True, on_delete=models.SET_NULL)
    # course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    # trainee1_name = models.CharField(verbose_name='ชื่อผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    # trainee1_id_card = models.CharField(verbose_name='เลขบัตรประชาชนผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    # trainee1_mobile = models.CharField(verbose_name='เบอร์มิอถือผู้เข้าอบรมคนที่1', max_length=100, null=True, blank=True)
    # trainee1_email = models.EmailField(verbose_name='อีเมลผู้เข้าอบรมคนที่1', null=True, blank=True)
    # trainee2_name = models.CharField(verbose_name='ชื่อผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    # trainee2_id_card = models.CharField(verbose_name='เลขบัตรประชาชนผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    # trainee2_mobile = models.CharField(verbose_name='เบอร์มิอถือผู้เข้าอบรมคนที่2', max_length=100, null=True, blank=True)
    # trainee2_email = models.EmailField(verbose_name='อีเมลผู้เข้าอบรมคนที่2', null=True, blank=True)
    
    # agreement = models.BooleanField(verbose_name='ยินยอมข้อตกลง', null=True, blank=True)

    def __str__(self):
        return self.regis_code


class FormInterview(models.Model):
    """ ฟอร์มสัมภาษณ์ """
    enterpise = models.ForeignKey(Enterpise, blank=True, null=True, on_delete=models.SET_NULL) 
    score1 = models.IntegerField(verbose_name='หมวดที่ 1 บทบาทของผู้บริหารในการนำองค์กร', null=True, blank=True)
    score2 = models.IntegerField(verbose_name='หมวดที่ 2. การวางแผนการดำเนินธุรกิจ', null=True, blank=True)
    score3 = models.IntegerField(verbose_name='หมวดที่ 3. การมุ่งเน้นลูกค้าและตลาด', null=True, blank=True)
    score4 = models.IntegerField(verbose_name='หมวดที่ 4. การวัด วิเคราะห์และจัดการความรู้', null=True, blank=True)
    score5 = models.IntegerField(verbose_name='หมวดที่ 5. การบริหารทรัพยากรบุคคล', null=True, blank=True)
    score6 = models.IntegerField(verbose_name='หมวดที่ 6. การจัดการกระบวนการ', null=True, blank=True)
    score7 = models.IntegerField(verbose_name='หมวดที่ 7. ผลลัพธ์ทางธุรกิจ', null=True, blank=True)
    score_total = models.IntegerField(verbose_name='คะแนนรวม', null=True, blank=True)
    interviewer = models.CharField(verbose_name='ผู้สัมภาษณ์', max_length=200, null=True, blank=True)
    interview_at = models.DateField(verbose_name='วันที่', auto_now_add=True)
    visit_summary = models.BooleanField(verbose_name='สรุปผลการลงคะแนน', default=True)

    def __str__(self):
        return '{}'.format(self.enterpise)

    def total_score(self):        
        return sum([self.score1, self.score2, self.score3, self.score4, self.score5, self.score6, self.score7])


class FormSiteVisit(models.Model):
    """ ฟอร์ม site visit """
    enterpise = models.ForeignKey(Enterpise, blank=True, null=True, on_delete=models.SET_NULL) 
    site_score1 = models.IntegerField(verbose_name='หมวดที่ 1 บทบาทของผู้บริหารในการนำองค์กร', null=True, blank=True)
    site_score2 = models.IntegerField(verbose_name='หมวดที่ 2. การวางแผนการดำเนินธุรกิจ', null=True, blank=True)
    site_score3 = models.IntegerField(verbose_name='หมวดที่ 3. การมุ่งเน้นลูกค้าและตลาด', null=True, blank=True)
    site_score4 = models.IntegerField(verbose_name='หมวดที่ 4. การวัด วิเคราะห์และจัดการความรู้', null=True, blank=True)
    site_score5 = models.IntegerField(verbose_name='หมวดที่ 5. การบริหารทรัพยากรบุคคล', null=True, blank=True)
    site_score6 = models.IntegerField(verbose_name='หมวดที่ 6. การจัดการกระบวนการ', null=True, blank=True)
    site_score7 = models.IntegerField(verbose_name='หมวดที่ 7. ผลลัพธ์ทางธุรกิจ', null=True, blank=True)
    score_total = models.IntegerField(verbose_name='คะแนนรวม', null=True, blank=True)
    visiter = models.CharField(verbose_name='ผู้ไปเยี่ยมชม', max_length=200, null=True, blank=True)
    visit_at = models.DateField(verbose_name='วันที่', auto_now_add=True)
    visit_summary = models.BooleanField(verbose_name='สรุปผลการลงคะแนน', default=True)

    def __str__(self):
        return '{}'.format(self.enterpise)

    def total_score(self):        
        return sum([self.site_score1, self.site_score2, self.site_score3, self.site_score4, self.site_score5, self.site_score6, self.site_score7])


class SmeCompetition(models.Model):
    """ MS ตารางหลักการเข้าประกวด sme12 """
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
        (11, 'ไม่เข้าชิงรางวัล'),
    ]
    
    enterpise = models.ForeignKey(Enterpise, blank=True, null=True, on_delete=models.SET_NULL) 
    competition = models.ForeignKey(Competition, blank=True, null=True, on_delete=models.SET_NULL)
    state = models.PositiveSmallIntegerField(verbose_name='สถานะการประกวด', choices=STATE, default=1)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)
    form_register = models.OneToOneField(FormRegister, blank=True, null=True, on_delete=models.SET_NULL)
    form_interview = models.OneToOneField(FormInterview, blank=True, null=True, on_delete=models.SET_NULL)
    form_site_visit = models.OneToOneField(FormSiteVisit, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        # if self.enterpise.name==None:
        #     return "ERROR-CUSTOMER NAME IS NULL"
        # return '{} - {}'.format(self.enterpise.name, self.competition.name)      
        return '{} - {}'.format(self.id, self.enterpise)

