# Generated by Django 3.1.7 on 2022-06-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Purchase_Order', '0009_auto_20220620_1507'),
        ('eProc_Form_Builder', '0002_auto_20220519_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='eformfielddata',
            name='po_item_guid',
            field=models.ForeignKey(blank=True, db_column='PO_ITEM_GUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Purchase_Order.poitem'),
        ),
    ]