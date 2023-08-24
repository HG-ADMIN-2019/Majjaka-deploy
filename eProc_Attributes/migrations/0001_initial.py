# Generated by Django 3.1.7 on 2023-08-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrgAttributesLevel',
            fields=[
                ('attr_level_guid', models.CharField(db_column='ATTR_LEVEL_GUID', max_length=32, primary_key=True, serialize=False, verbose_name='Attribute level guid')),
                ('version_number', models.PositiveIntegerField(db_column='VERSION_NUMBER', verbose_name='version_number')),
                ('object_type', models.CharField(db_column='OBJECT_TYPE', max_length=2, verbose_name='object type')),
                ('start_date', models.DateTimeField(db_column='START_DATE', null=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(db_column='END_DATE', null=True, verbose_name='end_date')),
                ('status', models.CharField(db_column='STATUS', max_length=1, null=True, verbose_name='Planning status')),
                ('low', models.CharField(db_column='LOW', max_length=60, null=True, verbose_name='Attribute value')),
                ('high', models.CharField(db_column='HIGH', max_length=60, null=True, verbose_name='Attribute values to')),
                ('attr_level_exclude', models.BooleanField(db_column='ATTR_LEVEL_EXCLUDE', default=False)),
                ('attr_level_default', models.BooleanField(db_column='ATTR_LEVEL_DEFAULT', default=False)),
                ('org_attr_created_at', models.DateTimeField(blank=True, db_column='ORG_ATTR_CREATED_AT', null=True)),
                ('org_attr_created_by', models.CharField(db_column='ORG_ATTR_CREATED_BY', max_length=30, null=True)),
                ('org_attr_changed_at', models.DateTimeField(blank=True, db_column='ORG_ATTR_CHANGED_AT', null=True)),
                ('org_attr_changed_by', models.CharField(db_column='ORG_ATTR_CHANGED_BY', max_length=30, null=True)),
                ('attribute_value_desc', models.CharField(db_column='attribute_value_desc', max_length=150, null=True, verbose_name='Attribute Value Desc')),
                ('extended_value', models.CharField(db_column='EXTENDED_VALUE', max_length=70, null=True, verbose_name='Extended Value')),
                ('del_ind', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'MTD_ORG_ATTR_LEVEL',
                'managed': True,
            },
        ),
    ]
