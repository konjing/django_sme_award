from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(verbose_name='ชื่อภูมิภาค', max_length=100)

    def __str__(self):
        return self.name


class Province(models.Model):
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    code = models.CharField(verbose_name='รหัสจังหวัด', max_length=20)
    name = models.CharField(verbose_name='ชื่อจังหวัด', max_length=100)

    def __str__(self):
        return self.name


class Amphur(models.Model):
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)
    code = models.CharField(verbose_name='รหัสอำเภอ', max_length=20)
    name = models.CharField(verbose_name='ชื่ออำเภอ', max_length=100)
    postcode = models.CharField(verbose_name='รหัสไปรษณีย์', max_length=20)

    def __str__(self):
        return self.name


class Tumbol(models.Model):
    amphur = models.ForeignKey(Amphur, null=True, on_delete=models.SET_NULL)
    code = models.CharField(verbose_name='รหัสตำบล', max_length=20)
    name = models.CharField(verbose_name='ชื่อตำบล', max_length=100)

    def __str__(self):
        return self.name


class BusinessType(models.Model):
    name = models.CharField(verbose_name='ประเภทธุรกิจ', max_length=200)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)

    def __str__(self):
        return self.name


class BusinessModel(models.Model):
    GROUP = [
        (1, 'นิติบุคคล'),
        (2, 'บุคคลธรรมดา'),
        (3, 'ได้รับการจดทะเบียน'),
    ]

    name = models.CharField(verbose_name='รูปแบบการจัดตั้งกิจการ', max_length=200)
    code = models.CharField(verbose_name='รหัส', max_length=10, null=True, blank=True)
    description = models.CharField(verbose_name='รายละเอียด', max_length=200, null=True, blank=True)
    model_group = models.PositiveSmallIntegerField(verbose_name='นิติบุคคล/บุคคลธรรมดา', choices=GROUP, default=1)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)

    def __str__(self):
        return '{} - {}'.format(self.model_group, self.name)


class BusinessGroup(models.Model):
    business_type = models.ForeignKey(BusinessType, null=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='กลุ่มธุรกิจ', max_length=200)
    etc_detail = models.CharField(verbose_name='รายละเอียดกลุ่มธุรกิจอื่นๆ', max_length=200,
                                   null=True, blank=True)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)


    def __str__(self):
        return self.name
       

class Owner(models.Model):
    name = models.CharField(verbose_name='ชื่อเจ้าของ', max_length=200) 
    card_id = models.CharField(verbose_name='เลขบัตรเจ้าของ', max_length=200, null=True, blank=True) 
    address_no = models.CharField(verbose_name='เลขที่', max_length=100, null=True, blank=True)
    mu = models.CharField(verbose_name='หมู่', max_length=100, null=True, blank=True)
    soi = models.CharField(verbose_name='ซอย', max_length=100, null=True, blank=True)
    street = models.CharField(verbose_name='ถนน', max_length=100, null=True, blank=True)    
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)
    amphur = models.ForeignKey(Amphur, null=True, on_delete=models.SET_NULL)
    tumbol = models.ForeignKey(Tumbol, null=True, on_delete=models.SET_NULL)
    postcode = models.CharField(verbose_name='รหัสไปรษณีย์', max_length=200, null=True, blank=True)
    tel = models.CharField(verbose_name='เบอร์ติดต่อเจ้าของ', max_length=200, null=True, blank=True)
    fax = models.CharField(verbose_name='แฟกซ์ติดต่อเจ้าของ', max_length=200, null=True, blank=True)
    mobile = models.CharField(verbose_name='เบอร์มือถือติดต่อเจ้าของ', max_length=200, null=True, blank=True)
    email = models.EmailField(verbose_name='อีเมลติดต่อเจ้าของ', null=True, blank=True)

    def __str__(self):
        return self.name


class Enterpise(models.Model):
    
    name = models.CharField(verbose_name='ชื่อสถานประกอบการ', max_length=200) 
    establish_date = models.DateField(verbose_name='วันก่อตั้งกิจการ', null=True, blank=True) 
    sme_code = models.CharField(verbose_name='รหัสสมาชิก สสว.', max_length=50, null=True, blank=True) 
    sme_connext_code = models.CharField(verbose_name='รหัสสมาชิก sme connext.', max_length=50, null=True, blank=True)
    address_no = models.CharField(verbose_name='เลขที่', max_length=100, null=True, blank=True)
    mu = models.CharField(verbose_name='หมู่', max_length=100, null=True, blank=True)
    soi = models.CharField(verbose_name='ซอย', max_length=100, null=True, blank=True)
    street = models.CharField(verbose_name='ถนน', max_length=100, null=True, blank=True)
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)
    amphur = models.ForeignKey(Amphur, null=True, on_delete=models.SET_NULL)
    tumbol = models.ForeignKey(Tumbol, null=True, on_delete=models.SET_NULL)
    postcode = models.CharField(verbose_name='รหัสไปรษณีย์', max_length=200, null=True, blank=True)
    tel = models.CharField(verbose_name='เบอร์ติดต่อ', max_length=200, null=True, blank=True)
    fax = models.CharField(verbose_name='แฟกซ์ติดต่อ', max_length=200, null=True, blank=True)
    email = models.EmailField(verbose_name='อีเมลติดต่อ', null=True, blank=True)
    website = models.CharField(verbose_name='เว็บไซต์ติดต่อ', max_length=200, null=True, blank=True)

    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    business_model = models.ForeignKey(BusinessModel, null=True, blank=True, on_delete=models.SET_NULL)
    bus_model_etc1 = models.CharField(verbose_name='นิติบุลคลอื่นๆ', max_length=200, null=True, blank=True)
    bus_model_etc2 = models.CharField(verbose_name='ได้รับการจดทะเบียนอื่นๆ', max_length=200, null=True, blank=True)
    juristic_id = models.CharField(verbose_name='เลขทะเบียนนิติบุคคล', max_length=20, null=True, blank=True)
    card_id = models.CharField(verbose_name='เลขที่บัตรประชาชน', max_length=20, null=True, blank=True)
    commercial_regis_number = models.CharField(verbose_name='เลขทะเบียนพาณิชย์', max_length=20, null=True, blank=True)
    regis_number = models.CharField(verbose_name='เลขทะเบียน', max_length=20, null=True, blank=True)

    contact_name = models.CharField(verbose_name='ชื่อผู้ติดต่อ', max_length=100, null=True, blank=True)
    contact_position = models.CharField(verbose_name='ตำแหน่งผู้ติดต่อ', max_length=100, null=True, blank=True)
    contact_tel = models.CharField(verbose_name='เบอร์ผู้ติดต่อ', max_length=30, null=True, blank=True)
    contact_email = models.EmailField(verbose_name='อีเมลผู้ติดต่อ', null=True, blank=True)

    business_type = models.ForeignKey(BusinessType, null=True, blank=True, on_delete=models.SET_NULL)
    business_group = models.ForeignKey(BusinessGroup, null=True, blank=True, on_delete=models.SET_NULL)
    business_group_etc = models.CharField(verbose_name='กลุ่มธุรกิจอื่นๆ', max_length=100, null=True, blank=True)
    product_info = models.TextField(verbose_name='ระบุสินค้า ยี่ห้อ และบริการโดยละเอียด', null=True, blank=True)
    material = models.TextField(verbose_name='วัตถุดิบในการผลิต', null=True, blank=True)
    otop = models.BooleanField(verbose_name='มีการผลิตสินค้า OTOP หรือไม่', null=True, blank=True)

    regis_cap = models.DecimalField(verbose_name='ทุนจดทะเบียน', decimal_places=2, max_digits=10, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(verbose_name='ชื่อรางวัล', max_length=200)
    name_eng = models.CharField(verbose_name='ชื่อรางวัล eng', null=True, blank=True, max_length=200)
    active = models.BooleanField(verbose_name='สถานะใช้งาน', default=True)

    def __str__(self):
        return self.name


