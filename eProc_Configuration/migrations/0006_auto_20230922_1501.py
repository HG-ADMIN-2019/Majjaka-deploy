# Generated by Django 3.1.7 on 2023-09-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Configuration', '0005_auto_20230922_1312'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='approverlimitvalue',
            unique_together={('client', 'app_code_id', 'app_types', 'company_id', 'approver_limit_value_source_system')},
        ),
        migrations.AlterUniqueTogether(
            name='spendlimitvalue',
            unique_together={('spend_code_id', 'client', 'company_id', 'spend_limit_value_source_system')},
        ),
    ]
