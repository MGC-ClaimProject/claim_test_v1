# Generated by Django 5.1.5 on 2025-02-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("claims", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="claim",
            name="applicant_signature",
            field=models.TextField(
                blank=True,
                help_text="Base64 인코딩된 서명 이미지 데이터",
                null=True,
                verbose_name="신청자 서명",
            ),
        ),
        migrations.AddField(
            model_name="claim",
            name="insured_signature",
            field=models.TextField(
                blank=True,
                help_text="Base64 인코딩된 서명 이미지 데이터",
                null=True,
                verbose_name="피보험자 서명",
            ),
        ),
    ]
