# Generated by Django 3.0.5 on 2020-05-23 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0011_remove_enterpise_regis_cap'),
        ('app_sme12', '0020_auto_20200523_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='forminterview',
            name='enterpise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.Enterpise'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score1',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 1 บทบาทของผู้บริหารในการนำองค์กร'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score2',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 2. การวางแผนการดำเนินธุรกิจ'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score3',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 3. การมุ่งเน้นลูกค้าและตลาด'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score4',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 4. การวัด วิเคราะห์และจัดการความรู้'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score5',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 5. การบริหารทรัพยากรบุคคล'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score6',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 6. การจัดการกระบวนการ'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='score7',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมวดที่ 7. ผลลัพธ์ทางธุรกิจ'),
        ),
        migrations.AddField(
            model_name='forminterview',
            name='visit_summary',
            field=models.BooleanField(default=True, verbose_name='สรุปผลการลงคะแนน'),
        ),
    ]