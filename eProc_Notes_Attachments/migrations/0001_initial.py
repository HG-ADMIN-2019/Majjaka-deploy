# Generated by Django 3.1.7 on 2022-05-19 14:53

from django.db import migrations, models
import django.db.models.deletion
import eProc_Notes_Attachments.models.notes_attachements_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eProc_Configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('guid', models.CharField(db_column='NOTE_GUID', max_length=32, primary_key=True, serialize=False)),
                ('item_num', models.PositiveIntegerField(db_column='ITEM_NUM', default=0, verbose_name='Item Number')),
                ('header_guid', models.CharField(db_column='HEADER_GUID', max_length=32, null=True)),
                ('item_guid', models.CharField(blank=True, db_column='ITEM_GUID', max_length=32, null=True)),
                ('doc_num', models.CharField(blank=True, db_column='DOC_NUMBER', max_length=10, null=True, verbose_name='DOC Number')),
                ('note_type', models.CharField(db_column='NOTE_TYPE', max_length=20, null=True)),
                ('note_type_flag', models.CharField(db_column='NOTE_TYPE_FLAG', max_length=1, null=True)),
                ('note_text', models.CharField(db_column='NOTE_TEXT', max_length=1000, null=True)),
                ('notes_created_at', models.DateTimeField(db_column='NOTES_CREATED_AT', null=True)),
                ('notes_created_by', models.CharField(db_column='NOTES_CREATED_BY', max_length=12, null=True)),
                ('notes_changed_at', models.DateTimeField(blank=True, db_column='NOTES_CHANGED_AT', null=True)),
                ('notes_changed_by', models.CharField(db_column='NOTES_CHANGED_BY', max_length=12, null=True)),
                ('notes_source_system', models.CharField(db_column='NOTES_SOURCE_SYSTEM', max_length=20)),
                ('notes_destination_system', models.CharField(db_column='NOTES_DESTINATION_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('document_type', models.ForeignKey(db_column='DOCUMENT_TYPE', default=None, on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.documenttype')),
            ],
            options={
                'db_table': 'MTD_NOTES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('guid', models.CharField(db_column='guid', max_length=32, primary_key=True, serialize=False)),
                ('item_num', models.PositiveIntegerField(db_column='ITEM_NUM', default=0, verbose_name='Item Number')),
                ('header_guid', models.CharField(db_column='HEADER_GUID', max_length=32)),
                ('item_guid', models.CharField(blank=True, db_column='ITEM_GUID', max_length=32, null=True)),
                ('doc_num', models.CharField(db_column='DOC_NUMBER', max_length=10, verbose_name='DOC Number')),
                ('title', models.CharField(db_column='TITLE', max_length=20)),
                ('doc_file', models.FileField(db_column='DOC_FILE', upload_to=eProc_Notes_Attachments.models.notes_attachements_model.Attachments.get_file_path)),
                ('attach_type_flag', models.CharField(db_column='ATTACH_TYPE_FLAG', max_length=1)),
                ('doc_format', models.CharField(db_column='DOC_FORMAT', max_length=255)),
                ('attachments_created_at', models.DateTimeField(db_column='ATTACHMENTS_CREATED_AT', null=True)),
                ('attachments_created_by', models.CharField(db_column='ATTACHMENTS_CREATED_BY', max_length=12, null=True)),
                ('attachments_changed_at', models.DateTimeField(blank=True, db_column='ATTACHMENTS_CHANGED_AT', null=True)),
                ('attachments_changed_by', models.CharField(db_column='ATTACHMENTS_CHANGED_BY', max_length=12, null=True)),
                ('attachments_source_system', models.CharField(db_column='ATTACHMENTS_SOURCE_SYSTEM', max_length=20)),
                ('attachments_destination_system', models.CharField(db_column='ATTACHMENTS_DESTINATION_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('document_type', models.ForeignKey(db_column='DOCUMENT_TYPE', default=None, on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.documenttype')),
            ],
            options={
                'db_table': 'MTD_ATTACHMENTS',
                'managed': True,
            },
        ),
    ]