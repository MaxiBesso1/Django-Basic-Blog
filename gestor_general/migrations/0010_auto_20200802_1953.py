# Generated by Django 3.0.8 on 2020-08-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_general', '0009_auto_20200801_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ansewer_post',
            name='id_create',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id_dad',
        ),
        migrations.AddField(
            model_name='ansewer_post',
            name='nickname_create',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='nickname_dad',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
