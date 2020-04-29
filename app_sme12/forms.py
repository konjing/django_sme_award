from django import forms
from app_backend.models import Province, Amphur, Tumbol, BusinessModel, BusinessGroup, BusinessType

class RegistrationForm(forms.Form):
    regis_code = forms.CharField(label='เลขสมัคร', max_length=20)

    ent_name = forms.CharField(label='ชื่อสถานประกอบการ', max_length=200)
    ent_establish_date = forms.DateField(label='วันที่จัดตั้งกิจการ') 
    ent_sme_code = forms.CharField(label='รหัสสมาชิก สสว.', max_length=50, required=False)
    ent_sme_connext_code = forms.CharField(label='รหัสสมาชิก SME CONNEXT', max_length=50, required=False)
    ent_address_no = forms.CharField(label='เลขที่', max_length=100)
    ent_mu = forms.CharField(label='หมู่', max_length=100, required=False)
    ent_soi = forms.CharField(label='ซอย', max_length=100, required=False)
    ent_street = forms.CharField(label='ถนน', max_length=100, required=False)
    ent_province = forms.ModelChoiceField(label='จังหวัด', queryset=Province.objects.all(), empty_label='-- โปรดเลือก --')
    ent_amphur = forms.ModelChoiceField(label='อำเภอ', queryset=Amphur.objects.all(), empty_label='-- โปรดเลือก --')
    ent_tumbol = forms.ModelChoiceField(label='ตำบล', queryset=Tumbol.objects.all(), empty_label='---------', required=False)
    ent_postcode = forms.CharField(label='รหัสไปรษณีย์', max_length=200)
    ent_tel = forms.CharField(label='โทรศัพท์', max_length=200)
    ent_fax = forms.CharField(label='โทรสาร', max_length=200, required=False)
    ent_email = forms.EmailField(label='อีเมล')
    ent_website = forms.CharField(label='เว็บไซต์', max_length=200, required=False)

    owner_name = forms.CharField(label='ชื่อ-นามสกุล', max_length=200) 
    owner_card_id = forms.CharField(label='เลขที่บัตรประจำตัวประชาชน', max_length=200) 
    owner_address_no = forms.CharField(label='เลขที่', max_length=100)
    owner_mu = forms.CharField(label='หมู่', max_length=100, required=False)
    owner_soi = forms.CharField(label='ซอย', max_length=100, required=False)
    owner_street = forms.CharField(label='ถนน', max_length=100, required=False)
    owner_province = forms.ModelChoiceField(label='จังหวัด', queryset=Province.objects.all(), empty_label='-- โปรดเลือก --')
    owner_amphur = forms.ModelChoiceField(label='อำเภอ', queryset=Amphur.objects.all(), empty_label='-- โปรดเลือก --')
    owner_tumbol = forms.ModelChoiceField(label='ตำบล', queryset=Tumbol.objects.all(), empty_label='---------', required=False)
    owner_postcode = forms.CharField(label='รหัสไปรษณีย์', max_length=200)
    owner_tel = forms.CharField(label='โทรศัพท์', max_length=200)
    owner_fax = forms.CharField(label='โทรสาร', max_length=200, required=False)
    owner_mobile = forms.CharField(label='โทรศัพท์มือถือ', max_length=200)
    owner_email = forms.EmailField(label='อีเมล')

    business_model = forms.ModelChoiceField(label='รูปแบบการจัดตั้งกิจการ', queryset=BusinessModel.objects.all().order_by('model_group'), empty_label='-- โปรดเลือก --', required=False)
    bus_model_etc1 = forms.CharField(label='นิติบุลคลอื่นๆ', max_length=200, required=False)
    bus_model_etc2 = forms.CharField(label='ได้รับการจดทะเบียนอื่นๆ', max_length=200, required=False)
    juristic_id = forms.CharField(label='เลขทะเบียนนิติบุคคล', max_length=20, required=False)
    card_id = forms.CharField(label='เลขที่บัตรประชาชน', max_length=20, required=False)
    commercial_regis_number = forms.CharField(label='เลขทะเบียนพาณิชย์', max_length=20, required=False)
    regis_number = forms.CharField(label='เลขทะเบียน', max_length=20, required=False)

    contact_name = forms.CharField(label='ชื่อ-นามสกุล', max_length=100)
    contact_position = forms.CharField(label='ตำแหน่ง', max_length=100)
    contact_tel = forms.CharField(label='โทรศัพท์มือถือ', max_length=30)
    contact_email = forms.EmailField(label='อีเมล')

    business_type = forms.ModelChoiceField(label='ประเภทกิจการ', queryset=BusinessType.objects.all(), empty_label='-- โปรดเลือก --')
    business_group = forms.ModelChoiceField(label='ประเภทกลุ่มธุรกิจ', queryset=BusinessGroup.objects.all(), empty_label='-- โปรดเลือก --')
    # business_group_etc = forms.CharField(label='กลุ่มธุรกิจอื่นๆ', max_length=100, required=False)
    product_info = forms.CharField(label='ระบุสินค้า ยี่ห้อ และบริการโดยละเอียด', widget=forms.Textarea, required=False)
    material = forms.CharField(label='วัตถุดิบในการผลิต', widget=forms.Textarea, required=False)
    # otop = forms.BooleanField(label='มีการผลิตสินค้า OTOP หรือไม่', required=False)

    # f_employ = forms.CharField(label='จำนวนการจ้างงาน', max_length=100, required=False)
    # f_revenue = forms.CharField(label='รายได้ต่อปี', max_length=100, required=False)
    
    # regis_cap = forms.DecimalField(label='ทุนจดทะเบียน/ทุนตั้งกิจการ(ปีที่เริ่มต้นกิจการ)', decimal_places=2, max_digits=10, required=False)
    # f_profit = forms.DecimalField(label='กำไร (ณ สิ้นปีก่อนหน้า)', max_digits=10, decimal_places=2, required=False)

    # f_news_from = forms.CharField(label='รับข่าวสารจากช่องทาง', max_length=100, required=False)
    # f_news_from_etc = forms.CharField(label='รับข่าวสารจากช่องทางอื่นๆ', max_length=100, required=False)

    # f_join_choice = forms.IntegerField(label='เลือกอบรมหรือประกวด', required=False)
    # f_training_course = forms.CharField(label='หลักสูตรอบรม', max_length=100, required=False)
    # f_trainee1_name = forms.CharField(label='ชื่อผู้เข้าอบรมคนที่1', max_length=100, required=False)
    # f_trainee1_id_card = forms.CharField(label='เลขบัตรประชาชนผู้เข้าอบรมคนที่1', max_length=100, required=False)
    # f_trainee1_mobile = forms.CharField(label='เบอร์มิอถือผู้เข้าอบรมคนที่1', max_length=100, required=False)
    # f_trainee1_email = forms.EmailField(label='อีเมลผู้เข้าอบรมคนที่1', required=False)
    # f_trainee2_name = forms.CharField(label='ชื่อผู้เข้าอบรมคนที่2', max_length=100, required=False)
    # f_trainee2_id_card = forms.CharField(label='เลขบัตรประชาชนผู้เข้าอบรมคนที่2', max_length=100, required=False)
    # f_trainee2_mobile = forms.CharField(label='เบอร์มิอถือผู้เข้าอบรมคนที่2', max_length=100, required=False)
    # f_trainee2_email = forms.EmailField(label='อีเมลผู้เข้าอบรมคนที่2', required=False)  

    # f_agreement = forms.BooleanField(label='ยินยอมข้อตกลง', required=False)
    # f_tsic_no = forms.CharField(label='เลข tsic', max_length=20, required=False)


 
    
    
