# Generated by Django 3.0.5 on 2020-05-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sme12', '0022_auto_20200525_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forminterview',
            name='interviewer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ผู้สัมภาษณ์'),
        ),
    ]