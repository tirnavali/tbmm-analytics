# Generated by Django 2.2.13 on 2020-07-29 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0014_referenceserviceanalytic_dijitalized_papers'),
    ]

    operations = [
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='report_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Raporun hazırlandığı tarih'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='reporter_identity',
            field=models.CharField(blank=True, max_length=60, verbose_name='Raporu hazırlayan personel adı soyadı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='reporter_title',
            field=models.CharField(blank=True, max_length=60, verbose_name='Raporu hazırlayan personel ünvanı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='date',
            field=models.DateField(verbose_name='Raporun ait olduğu tarih'),
        ),
    ]