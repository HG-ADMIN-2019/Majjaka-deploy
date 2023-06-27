# Generated by Django 3.1.7 on 2023-06-26 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eProc_Configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUserMonitoring',
            fields=[
                ('email_user_monitoring_guid', models.CharField(db_column='EMAIL_USER_MONITORING_GUID', max_length=32, primary_key=True, serialize=False)),
                ('object_type', models.CharField(db_column='OBJECT_TYPE', max_length=20)),
                ('username', models.CharField(db_column='USERNAME', max_length=20)),
                ('sender_email', models.EmailField(db_column='SENDER_EMAIL', max_length=100)),
                ('receiver_email', models.EmailField(db_column='RECEIVER_EMAIL', max_length=100)),
                ('email_status', models.PositiveIntegerField(db_column='EMAIL_STATUS')),
                ('error_type', models.CharField(db_column='ERROR_TYPE', max_length=20, null=True)),
                ('email_user_monitoring_created_by', models.CharField(db_column='EMAIL_USER_MONITORING_CREATED_BY', max_length=30, null=True)),
                ('email_user_monitoring_created_at', models.DateTimeField(auto_now_add=True, db_column='EMAIL_USER_MONITORING_CREATED_AT', max_length=50, null=True)),
                ('email_user_monitoring_changed_by', models.CharField(db_column='EMAIL_USER_MONITORING_CHANGED_BY', max_length=30, null=True)),
                ('email_user_monitoring_changed_at', models.DateTimeField(auto_now=True, db_column='EMAIL_USER_MONITORING_CHANGED_AT', max_length=50, null=True)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('email_contents_guid', models.ForeignKey(db_column='EMAIL_CONTENTS_GUID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.emailcontents')),
            ],
            options={
                'db_table': 'MTD_EMAIL_USER_MONITORING',
            },
        ),
        migrations.CreateModel(
            name='EmailSupplierMonitoring',
            fields=[
                ('email_supplier_monitoring_guid', models.CharField(db_column='EMAIL_SUPPLIER_MONITORING_GUID', max_length=32, primary_key=True, serialize=False)),
                ('object_type', models.CharField(db_column='OBJECT_TYPE', max_length=20)),
                ('doc_type', models.CharField(db_column='DOC_TYPE', max_length=10)),
                ('doc_number', models.CharField(db_column='DOC_NUMBER', max_length=10)),
                ('sender_email', models.EmailField(db_column='SENDER_EMAIL', max_length=100)),
                ('receiver_email', models.EmailField(db_column='RECEIVER_EMAIL', max_length=100)),
                ('email_status', models.PositiveIntegerField(db_column='EMAIL_STATUS')),
                ('error_type', models.CharField(db_column='ERROR_TYPE', max_length=20, null=True)),
                ('email_supplier_monitoring_created_by', models.CharField(db_column='EMAIL_SUPPLIER_MONITORING_CREATED_BY', max_length=30, null=True)),
                ('email_supplier_monitoring_created_at', models.DateTimeField(auto_now_add=True, db_column='EMAIL_SUPPLIER_MONITORING_CREATED_AT', max_length=50, null=True)),
                ('email_supplier_monitoring_changed_by', models.CharField(db_column='EMAIL_SUPPLIER_MONITORING_CHANGED_BY', max_length=30, null=True)),
                ('email_supplier_monitoring_changed_at', models.DateTimeField(auto_now=True, db_column='EMAIL_SUPPLIER_MONITORING_CHANGED_AT', max_length=50, null=True)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('email_contents_guid', models.ForeignKey(db_column='EMAIL_CONTENTS_GUID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.emailcontents')),
            ],
            options={
                'db_table': 'MTD_EMAIL_SUPPLIER_MONITORING',
            },
        ),
        migrations.CreateModel(
            name='EmailDocumentMonitoring',
            fields=[
                ('email_document_monitoring_guid', models.CharField(db_column='EMAIL_DOCUMENT_MONITORING_GUID', max_length=32, primary_key=True, serialize=False)),
                ('object_type', models.CharField(db_column='OBJECT_TYPE', max_length=20)),
                ('doc_type', models.CharField(db_column='DOC_TYPE', max_length=10)),
                ('doc_number', models.CharField(db_column='DOC_NUMBER', max_length=10)),
                ('sender_email', models.EmailField(db_column='SENDER_EMAIL', max_length=100)),
                ('receiver_email', models.EmailField(db_column='RECEIVER_EMAIL', max_length=100)),
                ('email_status', models.PositiveIntegerField(db_column='EMAIL_STATUS')),
                ('error_type', models.CharField(db_column='ERROR_TYPE', max_length=20, null=True)),
                ('email_document_monitoring_created_by', models.CharField(db_column='EMAIL_DOCUMENT_MONITORING_CREATED_BY', max_length=30, null=True)),
                ('email_document_monitoring_created_at', models.DateTimeField(auto_now_add=True, db_column='EMAIL_DOCUMENT_MONITORING_CREATED_AT', max_length=50, null=True)),
                ('email_document_monitoring_changed_by', models.CharField(db_column='EMAIL_DOCUMENT_MONITORING_CHANGED_BY', max_length=30, null=True)),
                ('email_document_monitoring_changed_at', models.DateTimeField(auto_now=True, db_column='EMAIL_DOCUMENT_MONITORING_CHANGED_AT', max_length=50, null=True)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('email_contents_guid', models.ForeignKey(db_column='EMAIL_CONTENTS_GUID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.emailcontents')),
            ],
            options={
                'db_table': 'MTD_EMAIL_DOCUMENT_MONITORING',
            },
        ),
    ]