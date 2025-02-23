# Generated by Django 5.1.5 on 2025-02-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_member_user_alter_member_relation"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="is_ad_agreed",
            field=models.BooleanField(default=False, verbose_name="광고성 정보 동의"),
        ),
    ]
