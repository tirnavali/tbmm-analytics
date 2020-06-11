# Generated by Django 2.2.13 on 2020-06-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from_out', models.IntegerField(default=0)),
                ('user_from_inside', models.IntegerField(default=0)),
                ('online_user_outside', models.IntegerField(default=0)),
                ('online_user_inside', models.IntegerField(default=0)),
                ('borrowed_books', models.IntegerField(default=0)),
                ('retired_books', models.IntegerField(default=0)),
                ('photocopy', models.IntegerField(default=0)),
                ('record_date', models.DateTimeField(verbose_name='date data entered')),
            ],
        ),
    ]
