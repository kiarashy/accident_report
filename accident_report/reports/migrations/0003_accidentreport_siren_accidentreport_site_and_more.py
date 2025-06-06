# Generated by Django 5.1.7 on 2025-03-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_accidentreport_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentreport',
            name='siren',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='site',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='spam_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='spam_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='spam_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='spam_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='spam_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='vic_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='vic_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
