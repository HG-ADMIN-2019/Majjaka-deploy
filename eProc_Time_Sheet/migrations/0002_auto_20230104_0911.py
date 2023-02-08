# Generated by Django 3.1.7 on 2023-01-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eProc_Time_Sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectefforts',
            name='del_ind',
            field=models.BooleanField(db_column='DEL_IND', default=False),
        ),
        migrations.AddField(
            model_name='projectefforts',
            name='project_efforts_changed_at',
            field=models.DateTimeField(db_column='project_efforts_changed_at', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectefforts',
            name='project_efforts_changed_by',
            field=models.CharField(db_column='PROJECT_EFFORTS_CHANGED_BY', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='projectefforts',
            name='project_efforts_created_at',
            field=models.DateTimeField(db_column='PROJECT_EFFORTS_CREATED_AT', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectefforts',
            name='project_efforts_created_by',
            field=models.CharField(db_column='PROJECT_EFFORTS_CREATED_BY', max_length=30, null=True),
        ),
    ]
