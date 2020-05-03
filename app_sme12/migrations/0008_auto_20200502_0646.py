# Generated by Django 3.0.5 on 2020-05-02 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0010_businessmodel_code'),
        ('app_sme12', '0007_auto_20200428_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formregister',
            name='employ',
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='รายได้ต่อปี')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='รหัส')),
                ('active', models.BooleanField(default=True, verbose_name='สถานะการใช้งาน')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.BusinessType')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='จำนวนการจ้างงาน')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='รหัส')),
                ('active', models.BooleanField(default=True, verbose_name='สถานะการใช้งาน')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_backend.BusinessType')),
            ],
        ),
        migrations.AddField(
            model_name='formregister',
            name='employment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_sme12.Employment'),
        ),
        migrations.AlterField(
            model_name='formregister',
            name='revenue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_sme12.Revenue'),
        ),
    ]
