# Generated by Django 5.1.5 on 2025-02-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("claims", "0002_claim_applicant_signature_claim_insured_signature"),
    ]

    operations = [
        migrations.AddField(
            model_name="claim",
            name="hospital_days",
            field=models.PositiveIntegerField(default=0, verbose_name="입원 일수"),
        ),
        migrations.AddField(
            model_name="claim",
            name="incident_type",
            field=models.CharField(
                choices=[("상해", "상해"), ("질병", "질병"), ("교통사고", "교통사고")],
                default="질병",
                max_length=10,
                verbose_name="사고 유형",
            ),
        ),
        migrations.AddField(
            model_name="claim",
            name="treatment_type",
            field=models.CharField(
                choices=[("입원", "입원"), ("통원", "통원")],
                default="통원",
                max_length=10,
                verbose_name="치료 유형",
            ),
        ),
    ]
