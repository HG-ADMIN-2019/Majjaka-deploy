# Generated by Django 3.1.7 on 2022-11-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Purchase_Order', '0011_auto_20221026_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='poitem',
            name='product_info_id',
            field=models.CharField(blank=True, db_column='PRODUCT_INFO_ID', max_length=40, null=True),
        ),
    ]