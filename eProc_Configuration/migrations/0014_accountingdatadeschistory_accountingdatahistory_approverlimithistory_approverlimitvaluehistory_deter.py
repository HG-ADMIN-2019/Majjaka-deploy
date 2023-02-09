# Generated by Django 3.1.7 on 2022-11-23 17:21

from django.db import migrations, models
import django.db.models.deletion
import eProc_Configuration.models.master_data


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Org_Model', '0001_initial'),
        ('eProc_Configuration', '0013_merge_20221123_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowACCHistory',
            fields=[
                ('workflow_acc_key', models.AutoField(db_column='WORKFLOW_ACC_KEY', primary_key=True, serialize=False)),
                ('workflow_acc_guid', models.CharField(db_column='WORKFLOW_ACC_GUID', max_length=32)),
                ('acc_value', models.CharField(db_column='ACC_VALUE', max_length=40)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('app_username', models.CharField(db_column='APP_USERNAME', max_length=16)),
                ('sup_company_id', models.CharField(db_column='SUP_COMPANY_ID', max_length=8)),
                ('sup_acc_value', models.CharField(db_column='SUP_ACC_VALUE', max_length=40)),
                ('workflow_acc_created_by', models.CharField(db_column='WORKFLOW_ACC_CREATED_BY', max_length=30, null=True)),
                ('workflow_acc_created_at', models.DateTimeField(db_column='WORKFLOW_ACC_CREATED_AT', max_length=50, null=True)),
                ('workflow_acc_changed_by', models.CharField(db_column='WORKFLOW_ACC_CHANGED_BY', max_length=30, null=True)),
                ('workflow_acc_changed_at', models.DateTimeField(db_column='WORKFLOW_ACC_CHANGED_AT', max_length=50, null=True)),
                ('workflow_acc_source_system', models.CharField(db_column='WORKFLOW_ACC_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('account_assign_cat', models.ForeignKey(db_column='ACCOUNT_ASSIGN_CAT', on_delete=django.db.models.deletion.DO_NOTHING, related_name='acc_asgn_cat', to='eProc_Configuration.accountassignmentcategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
                ('sup_acc_assign_cat', models.ForeignKey(db_column='SUP_ACC_ASSIGN_CAT', on_delete=django.db.models.deletion.DO_NOTHING, related_name='sup_acc_asgn_cat', to='eProc_Configuration.accountassignmentcategory')),
            ],
            options={
                'db_table': 'MMD_WF_ACC_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnspscCategoriesCustHistory',
            fields=[
                ('prod_cat_key', models.AutoField(db_column='PROD_CAT_KEY', primary_key=True, serialize=False)),
                ('prod_cat_guid', models.CharField(db_column='PROD_CAT_GUID', max_length=32)),
                ('unspsc_categories_cust_created_by', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_CREATED_BY', max_length=30, null=True)),
                ('unspsc_categories_cust_created_at', models.DateTimeField(db_column='UNSPSC_CATEGORIES_CUST_CREATED_AT', max_length=50, null=True)),
                ('unspsc_categories_cust_changed_by', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_CHANGED_BY', max_length=30, null=True)),
                ('unspsc_categories_cust_changed_at', models.DateTimeField(db_column='UNSPSC_CATEGORIES_CUST_CHANGED_AT', max_length=50, null=True)),
                ('unspsc_categories_cust_source_system', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('prod_cat_id', models.ForeignKey(db_column='PROD_CAT_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.unspsccategories')),
            ],
            options={
                'db_table': 'MMD_UNSPSC_CATEGORIES_CUST_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnspscCategoriesCustDescHistory',
            fields=[
                ('prod_cat_desc_key', models.AutoField(db_column='PROD_CAT_DESC_KEY', primary_key=True, serialize=False)),
                ('prod_cat_desc_guid', models.CharField(db_column='PROD_CAT_DESC_GUID', max_length=32)),
                ('category_desc', models.CharField(blank=True, db_column='CATEGORY_DESC', max_length=200, null=True, verbose_name='Category Description')),
                ('unspsc_categories_cust_desc_created_by', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_DESC_CREATED_BY', max_length=30, null=True)),
                ('unspsc_categories_cust_desc_created_at', models.DateTimeField(db_column='UNSPSC_CATEGORIES_CUST_DESC_CREATED_AT', max_length=50, null=True)),
                ('unspsc_categories_cust_desc_changed_by', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_DESC_CHANGED_BY', max_length=30, null=True)),
                ('unspsc_categories_cust_desc_changed_at', models.DateTimeField(db_column='UNSPSC_CATEGORIES_CUST_DESC_CHANGED_AT', max_length=50, null=True)),
                ('unspsc_categories_cust_desc_source_system', models.CharField(db_column='UNSPSC_CATEGORIES_CUST_DESC_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('language_id', models.ForeignKey(db_column='LANGUAGE_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.languages')),
                ('prod_cat_id', models.ForeignKey(db_column='PROD_CAT_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.unspsccategories')),
            ],
            options={
                'db_table': 'MMD_UNSPSC_CATEGORIES_CUST_DESC_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SupplierMasterHistory',
            fields=[
                ('supp_key', models.AutoField(db_column='SUPP_KEY', primary_key=True, serialize=False)),
                ('supp_guid', models.CharField(db_column='SUPP_GUID', max_length=32)),
                ('supplier_id', models.CharField(db_column='SUPPLIER_ID', max_length=10, verbose_name='Vendor Id')),
                ('supp_type', models.CharField(blank=True, db_column='SUPP_TYPE', max_length=35, null=True, verbose_name='Supplier Type')),
                ('name1', models.CharField(db_column='NAME1', max_length=40, verbose_name='Name 1')),
                ('name2', models.CharField(db_column='NAME2', max_length=40, null=True, verbose_name='Name 2')),
                ('supplier_username', models.CharField(db_column='SUPPLIER_USERNAME', max_length=16, null=True)),
                ('city', models.CharField(blank=True, db_column='CITY', max_length=40, null=True, verbose_name='City')),
                ('postal_code', models.CharField(blank=True, db_column='POSTAL_CODE', max_length=10, null=True, verbose_name='Postal Code')),
                ('street', models.CharField(db_column='STREET', max_length=60, null=True, verbose_name='Street')),
                ('landline', models.CharField(db_column='LANDLINE', max_length=30, null=True)),
                ('mobile_num', models.CharField(db_column='MOBILE_NUM', max_length=30, null=True)),
                ('fax', models.CharField(blank=True, db_column='FAX', max_length=20, null=True, verbose_name='Fax')),
                ('email', models.EmailField(db_column='EMAIL', max_length=100)),
                ('email1', models.EmailField(db_column='EMAIL1', max_length=100, null=True)),
                ('email2', models.EmailField(db_column='EMAIL2', max_length=100, null=True)),
                ('email3', models.EmailField(db_column='EMAIL3', max_length=100, null=True)),
                ('email4', models.EmailField(db_column='EMAIL4', max_length=100, null=True)),
                ('email5', models.EmailField(db_column='EMAIL5', max_length=100, null=True)),
                ('output_medium', models.CharField(blank=True, db_column='OUTPUT_MEDIUM', max_length=10, null=True, verbose_name='Output Medium')),
                ('search_term1', models.CharField(blank=True, db_column='SEARCH_TERM1', max_length=20, null=True, verbose_name='Search Term1')),
                ('search_term2', models.CharField(blank=True, db_column='SEARCH_TERM2', max_length=20, null=True, verbose_name='Search Term2')),
                ('duns_number', models.CharField(blank=True, db_column='DUNS_NUMBER', max_length=9, null=True, verbose_name='Duns Number')),
                ('block_date', models.DateField(db_column='BLOCK DATE', null=True, verbose_name='Block Date')),
                ('block', models.BooleanField(db_column='BLOCK', default=False)),
                ('delivery_days', models.CharField(blank=True, db_column='DELIVERY_DAYS', max_length=20, null=True)),
                ('is_active', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('registration_number', models.CharField(db_column='REGISTRATION_NUMBER', max_length=30, null=True)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('supplier_master_created_by', models.CharField(db_column='SUPPLIER_MASTER_CREATED_BY', max_length=30, null=True)),
                ('supplier_master_created_at', models.DateTimeField(db_column='SUPPLIER_MASTER_CREATED_AT', max_length=50, null=True)),
                ('supplier_master_changed_by', models.CharField(db_column='SUPPLIER_MASTER_CHANGED_BY', max_length=30, null=True)),
                ('supplier_master_changed_at', models.DateTimeField(db_column='SUPPLIER_MASTER_CHANGED_AT', max_length=50, null=True)),
                ('supplier_master_source_system', models.CharField(db_column='SUPPLIER_MASTER_SOURCE_SYSTEM', max_length=20)),
                ('pref_routing', models.CharField(blank=True, db_column='PREF_ROUTING', max_length=1, null=True, verbose_name='Preferred Routing')),
                ('lock_date', models.DateTimeField(blank=True, db_column='LOCK_DATE', null=True, verbose_name='Supplier will be locked on all Purch Orgs on this date')),
                ('global_duns', models.CharField(db_column='GLOBAL_DUNS', max_length=9, null=True, verbose_name='Global Duns Number')),
                ('domestic_duns', models.CharField(db_column='DOMESTIC_DUNS', max_length=9, null=True, verbose_name='Global Duns Number')),
                ('ics_code', models.CharField(blank=True, db_column='ICS_CODE', max_length=4, null=True, verbose_name='ICS code for vendor')),
                ('internal_ind', models.BooleanField(db_column='INTERNAL_IND', default=False, verbose_name='Internal Supplier Indicator')),
                ('sba_code', models.CharField(blank=True, db_column='SBA_CODE', max_length=2, null=True, verbose_name='SBA Code')),
                ('ethnicity', models.CharField(blank=True, db_column='ETHNICITY', max_length=2, null=True, verbose_name='PEthnicity/Gender Code')),
                ('hubzone', models.CharField(blank=True, db_column='HUBZONE', max_length=2, null=True, verbose_name='Hubzone')),
                ('no_vend_text', models.BooleanField(db_column='NO_VEND_TEXT', default=False, verbose_name='Flag indication supplier not able to receive Vendor Text')),
                ('agr_reg_no', models.CharField(blank=True, db_column='AGR_REG_NO', max_length=40, null=True, verbose_name='Agreement Registration Number')),
                ('no_mult_addr', models.BooleanField(db_column='NO_MULT_ADDR', default=False, verbose_name='Flag indication for multiple ordering addresses not support')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('country_code', models.ForeignKey(db_column='COUNTRY_CODE', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.country', verbose_name='Country')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
                ('language_id', models.ForeignKey(db_column='LANGUAGE_ID', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.languages', verbose_name='Language')),
            ],
            options={
                'db_table': 'MMD_SUPPLIERS_HISTORY',
                'managed': True,
            },
            bases=(models.Model, eProc_Configuration.models.master_data.DBQueriesSupplier),
        ),
        migrations.CreateModel(
            name='SpendLimitValueHistory',
            fields=[
                ('spend_lim_value_key', models.AutoField(db_column='SPEND_LIM_VALUE_KEY', primary_key=True, serialize=False)),
                ('spend_lim_value_guid', models.CharField(db_column='SPEND_LIM_VALUE_GUID', max_length=32)),
                ('spend_code_id', models.CharField(db_column='SPEND_CODE_ID', max_length=8)),
                ('upper_limit_value', models.PositiveIntegerField(db_column='UPPER_LIMIT_VALUE')),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('spend_limit_value_created_by', models.CharField(db_column='SPEND_LIMIT_VALUE_CREATED_BY', max_length=30, null=True)),
                ('spend_limit_value_created_at', models.DateTimeField(db_column='SPEND_LIMIT_VALUE_CREATED_AT', max_length=50, null=True)),
                ('spend_limit_value_changed_by', models.CharField(db_column='SPEND_LIMIT_VALUE_CHANGED_BY', max_length=30, null=True)),
                ('spend_limit_value_changed_at', models.DateTimeField(db_column='SPEND_LIMIT_VALUE_CHANGED_AT', max_length=50, null=True)),
                ('spend_limit_value_source_system', models.CharField(db_column='SPEND_LIMIT_VALUE_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
            ],
            options={
                'db_table': 'MMD_SPENDER_LIMIT_VALUE_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SpendLimitIdHistory',
            fields=[
                ('spend_key', models.AutoField(db_column='SPEND_KEY', primary_key=True, serialize=False)),
                ('spend_guid', models.CharField(db_column='SPEND_GUID', max_length=32)),
                ('spend_code_id', models.CharField(db_column='SPEND_CODE_ID', max_length=8)),
                ('spender_username', models.CharField(db_column='SPENDER_USERNAME', max_length=16)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('spend_limit_id_created_by', models.CharField(db_column='spend_limit_id_created_by', max_length=30, null=True)),
                ('spend_limit_id_created_at', models.DateTimeField(db_column='spend_limit_id_created_at', max_length=50, null=True)),
                ('spend_limit_id_changed_by', models.CharField(db_column='spend_limit_id_changed_by', max_length=30, null=True)),
                ('spend_limit_id_changed_at', models.DateTimeField(db_column='spend_limit_id_changed_at', max_length=50, null=True)),
                ('spend_limit_id_source_system', models.CharField(db_column='spend_limit_id_source_system', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MMD_SPENDER_LIMIT_ID_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrgPorgHistory',
            fields=[
                ('porg_key', models.AutoField(db_column='PORG_KEY', primary_key=True, serialize=False)),
                ('porg_guid', models.CharField(db_column='PORG_GUID', max_length=32)),
                ('porg_id', models.CharField(db_column='PORG_ID', max_length=8)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=100)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('org_porg_created_by', models.CharField(db_column='ORG_PORG_CREATED_BY', max_length=30, null=True)),
                ('org_porg_created_at', models.DateTimeField(db_column='ORG_PORG_CREATED_AT', max_length=50, null=True)),
                ('org_porg_changed_by', models.CharField(db_column='ORG_PORG_CHANGED_BY', max_length=30, null=True)),
                ('org_porg_changed_at', models.DateTimeField(db_column='ORG_PORG_CHANGED_AT', max_length=50, null=True)),
                ('org_porg_source_system', models.CharField(db_column='ORG_PORG_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('object_id', models.ForeignKey(db_column='OBJECT_ID', default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='eProc_Org_Model.orgmodel')),
            ],
            options={
                'db_table': 'MMD_ORG_PORG_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrgPGroupHistory',
            fields=[
                ('pgroup_key', models.AutoField(db_column='PGROUP_KEY', primary_key=True, serialize=False)),
                ('pgroup_guid', models.CharField(db_column='PGROUP_GUID', max_length=32)),
                ('pgroup_id', models.CharField(db_column='PGROUP_ID', max_length=8)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=100)),
                ('porg_id', models.CharField(db_column='PORG_ID', max_length=8)),
                ('org_pgroup_created_by', models.CharField(db_column='ORG_PGROUP_CREATED_BY', max_length=30, null=True)),
                ('org_pgroup_created_at', models.DateTimeField(db_column='ORG_PGROUP_CREATED_AT', max_length=50, null=True)),
                ('org_pgroup_changed_by', models.CharField(db_column='ORG_PGROUP_CHANGED_BY', max_length=30, null=True)),
                ('org_pgroup_changed_at', models.DateTimeField(db_column='ORG_PGROUP_CHANGED_AT', max_length=50, null=True)),
                ('org_pgroup_source_system', models.CharField(db_column='ORG_PGROUP_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('object_id', models.ForeignKey(db_column='OBJECT_ID', default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='eProc_Org_Model.orgmodel')),
            ],
            options={
                'db_table': 'MMD_ORG_PGROUP_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrgCompaniesHistory',
            fields=[
                ('company_key', models.AutoField(db_column='COMPANY_KEY', primary_key=True, serialize=False)),
                ('company_guid', models.CharField(db_column='COMPANY_GUID', max_length=32)),
                ('name1', models.CharField(db_column='NAME1', max_length=100)),
                ('name2', models.CharField(db_column='NAME2', max_length=100)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('org_companies_created_by', models.CharField(db_column='ORG_COMPANIES_CREATED_BY', max_length=30, null=True)),
                ('org_companies_created_at', models.DateTimeField(db_column='ORG_COMPANIES_CREATED_AT', max_length=50, null=True)),
                ('org_companies_changed_by', models.CharField(db_column='ORG_COMPANIES_CHANGED_BY', max_length=30, null=True)),
                ('org_companies_changed_at', models.DateTimeField(db_column='ORG_COMPANIES_CHANGED_AT', max_length=50, null=True)),
                ('org_companies_source_system', models.CharField(db_column='ORG_COMPANIES_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='Client', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('object_id', models.ForeignKey(db_column='OBJECT_ID', default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='eProc_Org_Model.orgmodel')),
            ],
            options={
                'db_table': 'MMD_ORG_COMPANIES_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetermineGLAccountHistory',
            fields=[
                ('det_gl_acc_key', models.AutoField(db_column='DET_GL_ACC_KEY', primary_key=True, serialize=False)),
                ('det_gl_acc_guid', models.CharField(db_column='DET_GL_ACC_GUID', max_length=32)),
                ('prod_cat_id', models.CharField(db_column='PROD_CAT_ID', max_length=20)),
                ('item_from_value', models.PositiveIntegerField(db_column='ITEM_FROM_VALUE', null=True)),
                ('item_to_value', models.PositiveIntegerField(db_column='ITEM_TO_VALUE', null=True)),
                ('gl_acc_num', models.CharField(db_column='GL_ACC_NUM', max_length=10, null=True)),
                ('gl_acc_default', models.BooleanField(db_column='GL_ACC_DEFAULT', default=False)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('determine_gl_account_created_by', models.CharField(db_column='DETERMINE_GL_ACCOUNT_CREATED_BY', max_length=30, null=True)),
                ('determine_gl_account_created_at', models.DateTimeField(db_column='DETERMINE_GL_ACCOUNT_CREATED_AT', max_length=50, null=True)),
                ('determine_gl_account_changed_by', models.CharField(db_column='DETERMINE_GL_ACCOUNT_CHANGED_BY', max_length=30, null=True)),
                ('determine_gl_account_changed_at', models.DateTimeField(db_column='DETERMINE_GL_ACCOUNT_CHANGED_AT', max_length=50, null=True)),
                ('determine_gl_account_source_system', models.CharField(db_column='DETERMINE_GL_ACCOUNT_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('account_assign_cat', models.ForeignKey(db_column='ACCOUNT_ASSIGN_CAT', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.accountassignmentcategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
            ],
            options={
                'db_table': 'MMD_DET_GL_ACC_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ApproverLimitValueHistory',
            fields=[
                ('app_lim_dec_key', models.AutoField(db_column='APP_LIM_DEC_KEY', primary_key=True, serialize=False)),
                ('app_lim_dec_guid', models.CharField(db_column='APP_LIM_DEC_GUID', max_length=32)),
                ('app_code_id', models.CharField(db_column='APP_CODE_ID', max_length=8)),
                ('upper_limit_value', models.PositiveIntegerField(db_column='UPPER_LIMIT_VALUE', null=True)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('approver_limit_value_created_by', models.CharField(db_column='APPROVER_LIMIT_VALUE_CREATED_BY', max_length=30, null=True)),
                ('approver_limit_value_created_at', models.DateTimeField(db_column='APPROVER_LIMIT_VALUE_CREATED_AT', max_length=50, null=True)),
                ('approver_limit_value_changed_by', models.CharField(db_column='APPROVER_LIMIT_VALUE_CHANGED_BY', max_length=30, null=True)),
                ('approver_limit_value_changed_at', models.DateTimeField(db_column='APPROVER_LIMIT_VALUE_CHANGED_AT', max_length=50, null=True)),
                ('approver_limit_value_source_system', models.CharField(db_column='APPROVER_LIMIT_VALUE_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('app_types', models.ForeignKey(db_column='APP_TYPES', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.approvertype')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
            ],
            options={
                'db_table': 'MMD_APPROVER_LIMIT_VALUE_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ApproverLimitHistory',
            fields=[
                ('app_key', models.AutoField(db_column='APP_KEY', primary_key=True, serialize=False)),
                ('app_guid', models.CharField(db_column='APP_GUID', max_length=32)),
                ('approver_username', models.CharField(db_column='APPROVER_USERNAME', max_length=16)),
                ('app_code_id', models.CharField(db_column='APP_CODE_ID', max_length=8)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('approver_limit_created_by', models.CharField(db_column='APPROVER_LIMIT_CREATED_BY', max_length=30, null=True)),
                ('approver_limit_created_at', models.DateTimeField(db_column='APPROVER_LIMIT_CREATED_AT', max_length=50, null=True)),
                ('approver_limit_changed_by', models.CharField(db_column='APPROVER_LIMIT_CHANGED_BY', max_length=30, null=True)),
                ('approver_limit_changed_at', models.DateTimeField(db_column='APPROVER_LIMIT_CHANGED_AT', max_length=50, null=True)),
                ('approver_limit_source_system', models.CharField(db_column='APPROVER_LIMIT_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MMD_APPROVER_LIMIT_ID_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AccountingDataHistory',
            fields=[
                ('account_assign_key', models.AutoField(db_column='ACCOUNT_ASSIGN_KEY', primary_key=True, serialize=False)),
                ('account_assign_guid', models.CharField(db_column='ACCOUNT_ASSIGN_GUID', max_length=32)),
                ('account_assign_value', models.CharField(db_column='ACC_ASSIGN_VALUE', max_length=40)),
                ('valid_from', models.DateField(db_column='VAILD_FROM')),
                ('valid_to', models.DateField(db_column='VAILD_TO')),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('accounting_data_created_by', models.CharField(db_column='ACCOUNTING_DATA_CREATED_BY', max_length=30, null=True)),
                ('accounting_data_created_at', models.DateTimeField(db_column='ACCOUNTING_DATA_CREATED_AT', max_length=50, null=True)),
                ('accounting_data_changed_by', models.CharField(db_column='ACCOUNTING_DATA_CHANGED_BY', max_length=30, null=True)),
                ('accounting_data_changed_at', models.DateTimeField(db_column='ACCOUNTING_DATA_CHANGED_AT', max_length=50, null=True)),
                ('accounting_data_source_system', models.CharField(db_column='ACCOUNTING_DATA_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('account_assign_cat', models.ForeignKey(db_column='ACCOUNT_ASSIGN_CAT', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.accountassignmentcategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MMD_ACCOUNTING_DATA_HISTORY',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AccountingDataDescHistory',
            fields=[
                ('acc_desc_key', models.AutoField(db_column='ACC_DESC_KEY', primary_key=True, serialize=False)),
                ('acc_desc_guid', models.CharField(db_column='ACC_DESC_GUID', max_length=32)),
                ('account_assign_value', models.CharField(db_column='ACCOUNT_ASSIGN_VALUE', max_length=40)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=255)),
                ('company_id', models.CharField(db_column='COMPANY_ID', max_length=8)),
                ('accounting_data_desc_created_by', models.CharField(db_column='ACCOUNTING_DATA_DESC_CREATED_BY', max_length=30, null=True)),
                ('accounting_data_desc_created_at', models.DateTimeField(db_column='ACCOUNTING_DATA_DESC_CREATED_AT', max_length=50, null=True)),
                ('accounting_data_desc_changed_by', models.CharField(db_column='ACCOUNTING_DATA_DESC_CHANGED_BY', max_length=30, null=True)),
                ('accounting_data_desc_changed_at', models.DateTimeField(db_column='ACCOUNTING_DATA_DESC_CHANGED_AT', max_length=50, null=True)),
                ('accounting_data_desc_source_system', models.CharField(db_column='ACCOUNTING_DATA_DESC_SOURCE_SYSTEM', max_length=20)),
                ('del_ind', models.BooleanField(default=False)),
                ('account_assign_cat', models.ForeignKey(db_column='ACCOUNT_ASSIGN_CAT', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.accountassignmentcategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('language_id', models.ForeignKey(db_column='LANGUAGE_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.languages')),
            ],
            options={
                'db_table': 'MMD_ACC_DATA_DESC_HISTORY',
                'managed': True,
            },
        ),
    ]