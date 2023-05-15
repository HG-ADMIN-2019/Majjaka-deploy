from eProc_Basic.Utilities.constants.constants import CONST_PROJECT_ID
from eProc_Basic.Utilities.functions.django_query_set import DjangoQueries
from eProc_Basic.Utilities.functions.guid_generator import guid_generator
from eProc_Basic.Utilities.global_defination import global_variables
from eProc_Configuration.models.application_data import ProjectDetails
from eProc_Time_Sheet.models import ProjectEfforts
from datetime import datetime, date, timedelta
from datetime import date, timedelta

django_query_instance = DjangoQueries()


def save_project_to_db(project_data):
    """

    """
    project_detail = project_data['project_data']
    if project_data['project_action'] == 'UPDATE':
        django_query_instance.django_update_query(ProjectDetails,
                                                  {'client': global_variables.GLOBAL_CLIENT,
                                                   'project_id': project_detail['project_id']},
                                                  {'project_name': project_detail['project_name'],
                                                   'project_desc': project_detail['project_description'],
                                                   'start_date': project_detail['start_date'],
                                                   'end_date': project_detail['end_date']})
    else:
        project_dictionary = {'project_detail_guid': guid_generator(),
                              'client': global_variables.GLOBAL_CLIENT,
                              'project_id': project_detail['project_id'],
                              'project_name': project_detail['project_name'],
                              'project_desc': project_detail['project_description'],
                              'start_date': project_detail['start_date'],
                              'end_date': project_detail['end_date']}
        django_query_instance.django_create_query(ProjectDetails, project_dictionary)
    project_data_response = django_query_instance.django_filter_query(ProjectDetails,
                                                                      {'del_ind': False,
                                                                       'client': global_variables.GLOBAL_CLIENT},
                                                                      None, None)

    return project_data_response


def get_project_filter_list(project_id):
    """

    """
    project_details = django_query_instance.django_filter_query(ProjectDetails, {'project_id': project_id},
                                                                ['project_id'],
                                                                None, )

    return project_details


# def get_efforts_filter_list(project_id,default_calendar_id):
#     project_efforts = django_query_instance.django_filter_query_with_entry_count(ProjectEfforts,{
#                                                                 'username': global_variables.GLOBAL_LOGIN_USERNAME,
#                                                                 'calender_id': default_calendar_id,
#                                                                 'project_id': project_id})
#     return project_efforts


def get_efforts_filter_list(project_id):
    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # get the start date of the current week
    week_end = week_start + timedelta(days=6)  # get the end date of the current week

    filter_query = {'project_id': project_id, 'effort_date__gte': week_start, 'effort_date__lte': week_end}

    project_efforts = django_query_instance.django_filter_query(ProjectEfforts, filter_query,
                                                                ['project_id', 'username', 'calender_id'],
                                                                None)

    return project_efforts
