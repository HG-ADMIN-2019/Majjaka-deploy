# Generated by Django 3.1.7 on 2023-04-26 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Configuration', '0019_auto_20230104_0911'),
        ('eProc_Org_Model', '0001_initial'),
        ('eProc_Suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgSuppliersHistory',
            fields=[
                ('orgsupp_key', models.AutoField(db_column='ORGSUPP_KEY', primary_key=True, serialize=False)),
                ('guid', models.CharField(db_column='GUID', default=None, max_length=32)),
                ('supplier_id', models.CharField(db_column='SUPPLIER_ID', max_length=10, null=True, verbose_name='Vendor Id')),
                ('sup_address_number', models.PositiveIntegerField(db_column='SUP_ADDRESS_NUMBER', null=True)),
                ('payment_term_key', models.CharField(blank=True, db_column='PAYTERM_KEY', max_length=4, null=True, verbose_name='Payment Term')),
                ('gr_ind', models.BooleanField(db_column='GR_IND', null=True, verbose_name='Gr ind')),
                ('ir_gr_ind', models.BooleanField(db_column='IR_GR_IND', null=True, verbose_name='Ir Gr ind')),
                ('ir_ind', models.BooleanField(db_column='IR_IND', null=True, verbose_name='ir ind')),
                ('po_resp', models.BooleanField(db_column='PO_RESP', null=True, verbose_name='PO Response')),
                ('asn_ind', models.BooleanField(db_column='ASN_IND', null=True, verbose_name='Advance shipment Notice')),
                ('ship_notif_exp', models.BooleanField(db_column='SHIPPING_NOTIF_EXPECTED', default=False)),
                ('purch_block', models.BooleanField(db_column='PURCHASE_BLOCK', default=False)),
                ('porg_id', models.CharField(db_column='P_ORG_ID', max_length=8)),
                ('org_supp_created_at', models.DateTimeField(blank=True, db_column='ORG_SUPP_CREATED_AT', null=True)),
                ('org_supp_created_by', models.CharField(db_column='ORG_SUPP_CREATED_BY', max_length=30, null=True)),
                ('org_supp_changed_at', models.DateTimeField(blank=True, db_column='ORG_SUPP_CHANGED_AT', null=True)),
                ('org_supp_changed_by', models.CharField(db_column='ORG_SUPP_CHANGED_BY', max_length=30, null=True)),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('currency_id', models.ForeignKey(db_column='CURRENCY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.currency')),
                ('incoterm_key', models.ForeignKey(blank=True, db_column='INCOTERM_KEY', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Configuration.incoterms', verbose_name='Incoterm1')),
                ('porg_object_id', models.ForeignKey(db_column='OBJECT_ID', default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='eProc_Org_Model.orgmodel')),
            ],
            options={
                'db_table': 'MTD_ORG_SUPPLIERS_HISTORY',
                'managed': True,
            },
        ),
    ]
