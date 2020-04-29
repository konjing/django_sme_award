# Generated by Django 3.0.5 on 2020-04-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0008_auto_20200428_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessmodel',
            name='model_group',
            field=models.PositiveSmallIntegerField(choices=[(1, 'นิติบุคคล'), (2, 'บุคคลธรรมดา'), (3, 'ได้รับการจดทะเบียน')], default=1, verbose_name='นิติบุคคล/บุคคลธรรมดา'),
        ),
    ]
