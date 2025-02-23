# Generated by Django 5.1.5 on 2025-01-21 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("members", "0002_alter_member_relation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Claim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("incident_date", models.DateField(verbose_name="사고 발생일")),
                ("symptoms", models.TextField(verbose_name="증상")),
                (
                    "claim_insurers",
                    models.JSONField(
                        default=list,
                        help_text="청구 대상 보험사 리스트를 JSON 형식으로 저장합니다.",
                        verbose_name="청구 보험사 리스트",
                    ),
                ),
                (
                    "is_required_agreement",
                    models.BooleanField(default=False, verbose_name="필수 동의 여부"),
                ),
                (
                    "bank",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="은행명"
                    ),
                ),
                (
                    "account",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="계좌 번호"
                    ),
                ),
                (
                    "is_same_as_payout_account",
                    models.BooleanField(
                        default=True, verbose_name="출금 계좌와 동일 여부"
                    ),
                ),
                (
                    "claim_status",
                    models.CharField(
                        choices=[
                            ("draft", "작성중"),
                            ("completed", "작성완료"),
                            ("sending", "발송중"),
                            ("send_error", "발송에러"),
                            ("sent", "발송완료"),
                            ("claimed", "청구 완료"),
                            ("cancelled", "청구 취소"),
                            ("received", "수령 완료"),
                        ],
                        default="draft",
                        max_length=20,
                        verbose_name="청구 상태",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일"),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="claims",
                        to="members.member",
                        verbose_name="피보험자",
                    ),
                ),
            ],
            options={
                "verbose_name": "보험 청구",
                "verbose_name_plural": "보험 청구들",
            },
        ),
        migrations.CreateModel(
            name="AddDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        upload_to="claim_documents/", verbose_name="추가 문서"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일"),
                ),
                (
                    "claim",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="claims.claim",
                        verbose_name="청구",
                    ),
                ),
            ],
            options={
                "verbose_name": "추가 문서",
                "verbose_name_plural": "추가 문서들",
            },
        ),
    ]
