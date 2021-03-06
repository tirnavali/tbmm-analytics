# Generated by Django 2.2.13 on 2020-07-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0005_auto_20200722_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='depo_used_book',
            field=models.IntegerField(default=0, verbose_name='Depodan çıkartılan kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='depo_used_journal',
            field=models.IntegerField(default=0, verbose_name='Depodan çıkartılan dergi sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='depo_used_newspaper',
            field=models.IntegerField(default=0, verbose_name='Depodan çıkartılan gazete sayısı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='microfilm_mp',
            field=models.IntegerField(default=0, verbose_name='Mikrofilm kullanmış vekil sayısı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='microfilm_patron_inside',
            field=models.IntegerField(default=0, verbose_name='Mikrofilm kullanmış kurum içi personel sayısı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='microfilm_patron_outside',
            field=models.IntegerField(default=0, verbose_name='Mikrofim kullanmış kurum dışı personel sayısı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='microfilm_retired_mp',
            field=models.IntegerField(default=0, verbose_name='Mikrofilm kullanmış emekli vekil sayısı.'),
        ),
        migrations.AlterField(
            model_name='referenceserviceanalytic',
            name='user_from_out',
            field=models.IntegerField(default=0, verbose_name='Dışarıdan gelen kullanıcı sayısı.'),
        ),
    ]
