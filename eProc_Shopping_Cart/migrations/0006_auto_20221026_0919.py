# Generated by Django 3.1.7 on 2022-10-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Shopping_Cart', '0005_scheader_follow_on_doc_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemdetails',
            name='discount_id',
            field=models.CharField(db_column='DISCOUNT_ID', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='cartitemdetails',
            name='variant_id',
            field=models.CharField(db_column='VARIANT_ID', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='scitem',
            name='discount_id',
            field=models.CharField(db_column='DISCOUNT_ID', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='scitem',
            name='variant_id',
            field=models.CharField(db_column='VARIANT_ID', max_length=40, null=True),
        ),
    ]
