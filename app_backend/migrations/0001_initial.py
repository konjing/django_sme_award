# Generated by Django 3.0.5 on 2020-04-22 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='กลุ่มธุรกิจ')),
                ('etc_detail', models.CharField(blank=True, max_length=200, null=True, verbose_name='รายละเอียดกลุ่มธุรกิจอื่นๆ')),
                ('active', models.BooleanField(default=True, verbose_name='สถานะใช้งาน')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='รูปแบบการจัดตั้งกิจการ')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='รายละเอียด')),
                ('active', models.BooleanField(default=True, verbose_name='สถานะใช้งาน')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ประเภทธุรกิจ')),
                ('active', models.BooleanField(default=True, verbose_name='สถานะใช้งาน')),
            ],
        ),
        
        migrations.CreateModel(
            name='Enterpise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ชื่อสถานประกอบการ')),
                ('establish_date', models.DateField(verbose_name='ก่อตั้งกิจการ')),
                ('sme_code', models.CharField(max_length=50, verbose_name='รหัสสมาชิก สสว.')),
                ('sme_connext_code', models.CharField(max_length=50, verbose_name='รหัสสมาชิก sme connext.')),
                ('owner_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='ชื่อเจ้าของ')),
                ('owner_card_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='เลขบัตรเจ้าของ')),
                ('bus_model_etc1', models.CharField(blank=True, max_length=200, null=True, verbose_name='นิติบุลคลอื่นๆ')),
                ('bus_model_etc2', models.CharField(blank=True, max_length=200, null=True, verbose_name='ได้รับการจดทะเบียนอื่นๆ')),
                ('juristic_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='เลขทะเบียนนิติบุคคล')),
                ('card_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='เลขที่บัตรประชาชน')),
                ('commercial_regis_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='เลขทะเบียนพาณิชย์')),
                ('regis_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='เลขทะเบียน')),
                ('business_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.BusinessGroup')),
                ('business_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.BusinessModel')),
            ],
        ),
        migrations.AddField(
            model_name='businessgroup',
            name='business_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.BusinessType'),
        ),
    ]
