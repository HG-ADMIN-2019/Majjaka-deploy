from django.shortcuts import render
from eProc_Attributes.Utilities.attributes_generic import OrgAttributeValues
from eProc_Basic.Utilities.constants.constants import CONST_CALENDAR_ID, CONST_PROJECT_ID, \
    CONST_TIME_SHEET_UI_MESSAGE_LIST
from eProc_Basic.Utilities.functions.django_query_set import DjangoQueries
from eProc_Basic.Utilities.global_defination import global_variables
from eProc_Configuration.Utilities.application_settings_generic import get_ui_messages
from eProc_Configuration.models import ProjectDetails
from eProc_Projects.Utilities.project_specific import get_project_filter_list
from eProc_Shopping_Cart.context_processors import update_user_info
from eProc_User_Settings.Utilities.user_settings_generic import get_object_id_list_user
django_query_instance = DjangoQueries()

def get_project_details1(request):
    django_query_instance = DjangoQueries()
    update_user_info(request)
    object_id_list = get_object_id_list_user(global_variables.GLOBAL_CLIENT, global_variables.GLOBAL_LOGIN_USER_OBJ_ID)
    org_attr_value_instance = OrgAttributeValues()
    project_id = OrgAttributeValues.get_user_attr_value_list_by_attr_id(object_id_list,
                                                                        CONST_PROJECT_ID)
    default_calendar_id = org_attr_value_instance.get_user_default_attr_value_list_by_attr_id(object_id_list,
                                                                                              CONST_CALENDAR_ID)[1]
    filter_query = {'client': global_variables.GLOBAL_CLIENT, 'del_ind': False}
    project_details = get_project_filter_list(filter_query, 10)

    context = {
        'inc_nav': True,
        'inc_footer': True,
        'project_id': project_id,
        'default_calendar_id': default_calendar_id,
        'is_slide_menu': True,
        'is_home_active': False,
        'project_details': project_details
    }
    return render(request, 'Time_sheet/enter_time_sheet1.html', context)


def get_project_details(request):
    # Fetch Project data
    django_query_instance = DjangoQueries()
    update_user_info(request)
    object_id_list = get_object_id_list_user(global_variables.GLOBAL_CLIENT, global_variables.GLOBAL_LOGIN_USER_OBJ_ID)
    org_attr_value_instance = OrgAttributeValues()
    project_id = OrgAttributeValues.get_user_attr_value_list_by_attr_id(object_id_list,
                                                                        CONST_PROJECT_ID)
    default_calendar_id = org_attr_value_instance.get_user_default_attr_value_list_by_attr_id(object_id_list,
                                                                                              CONST_CALENDAR_ID)[1]
    filter_query = {'client': global_variables.GLOBAL_CLIENT, 'del_ind': False}
    project_details = get_project_filter_list(filter_query, 10)

    context = {
        'inc_nav': True,
        'inc_footer': True,
        'project_id': project_id,
        'default_calendar_id': default_calendar_id,
        'is_slide_menu': True,
        'is_home_active': False,
        'project_details': project_details
    }

    return render(request, 'Time_sheet/enter_time_sheet1.html', context)
