# Generated by Django 3.0.5 on 2020-05-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sme12', '0008_auto_20200502_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='agriculture',
            field=models.IntegerField(blank=True, max_length=40, null=True, verbose_name='จำนวนจ้างสำหรับธุรกิจเกษตร'),
        ),
    ]