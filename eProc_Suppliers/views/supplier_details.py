"""Copyright (c) 2020 Hiranya Garbha, Inc.
    Name:
        supplier_details.py
    Usage:
        Story SP12-10
        Function to get the supplier details
        Taking the supplier id and getting details and rendering back to the supplier details pop-up page
        We have the function to save the changes in Supplier details pop-up back to the data base
     Author:
        Varsha Prasad
"""
import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from eProc_Basic.Utilities.functions.django_query_set import DjangoQueries, bulk_create_entry_db
from eProc_Basic.Utilities.functions.encryption_util import decrypt
from eProc_Basic.Utilities.functions.get_db_query import getClients
from eProc_Basic.Utilities.functions.json_parser import JsonParser
from eProc_Basic.Utilities.functions.messages_config import get_msg_desc, get_message_desc
from eProc_Basic.Utilities.global_defination import global_variables
from eProc_Basic.Utilities.messages.messages import MSG177, MSG178
from eProc_Basic_Settings.views import JsonParser_obj
from eProc_Configuration.models import *
from eProc_Registration.Utilities.registration_generic import save_supplier_image, save_supplier_data
from eProc_Shopping_Cart.context_processors import update_user_info
from eProc_Basic.Utilities.functions.guid_generator import guid_generator
from eProc_Suppliers.models.suppliers_model import OrgSuppliers

django_query_instance = DjangoQueries()


@login_required
@transaction.atomic
def update_suppliers_basic_details(request):
    message = ''
    update_user_info(request)
    if request.method == 'POST':
        print(request.FILES)
        message, encrypted_supp = save_supplier_data(request)

        if 'supplier_image' in request.FILES:
            supplier_file = request.FILES['supplier_image']
            supplier_id = request.POST['supplier_id']
            supplier_image_name = request.FILES['supplier_image'].name
            save_supplier_image(supplier_file, supplier_id, supplier_image_name)

    return JsonResponse({'message': message, 'encrypted_supplier': encrypted_supp})


@transaction.atomic
def update_supplier_purch_details(request):
    error_msg = ''
    supp_org_data = JsonParser().get_json_from_req(request)
    # supplier_id = org_data['supp_id']
    org_sup_db_list = []
    for org_data in supp_org_data:
        if not django_query_instance.django_existence_check(OrgSuppliers,
                                                            {'porg_id': org_data['porg_id'],
                                                             'del_ind': False
                                                             }):
            guid = guid_generator()
            org_sup_db_dictionary = {'guid': guid,
                                     'supplier_id': org_data['supp_id'],
                                     'payment_term_key': org_data['payment_term'],
                                     'incoterm_key': django_query_instance.django_get_query(Incoterms, {
                                         'incoterm_key': org_data['incoterm']}),
                                     'currency_id': django_query_instance.django_get_query(Currency, {
                                         'pk': org_data['currency_id']}),
                                     'ir_gr_ind': org_data['gr_inv_vrf'],
                                     'ir_ind': org_data['inv_conf_exp'],
                                     'gr_ind': org_data['gr_conf_exp'],
                                     'po_resp': org_data['po_resp'],
                                     'ship_notif_exp': org_data['ship_notif_exp'],
                                     'purch_block': org_data['purch_block'],
                                     'porg_id': org_data['porg_id'],
                                     'client_id': getClients(request)
                                     }
            org_sup_db_list.append(org_sup_db_dictionary)
        else:
            django_query_instance.django_update_query(OrgSuppliers,
                                                      {'porg_id': org_data['porg_id'],
                                                       'client': getClients(request)},
                                                      {'supplier_id': org_data['supp_id'],
                                                       'payment_term_key': org_data['payment_term'],
                                                       'incoterm_key': django_query_instance.django_get_query(Incoterms,
                                                                                                              {
                                                                                                                  'incoterm_key':
                                                                                                                      org_data[
                                                                                                                          'incoterm']}),
                                                       'currency_id': django_query_instance.django_get_query(Currency, {
                                                           'pk': org_data['currency_id']}),
                                                       'ir_gr_ind': org_data['gr_inv_vrf'],
                                                       'ir_ind': org_data['inv_conf_exp'],
                                                       'gr_ind': org_data['gr_conf_exp'],
                                                       'po_resp': org_data['po_resp'],
                                                       'ship_notif_exp': org_data['ship_notif_exp'],
                                                       'purch_block': org_data['purch_block'],
                                                       'porg_id': org_data['porg_id'],
                                                       'client_id': getClients(request),
                                                       })
        if org_sup_db_list:
            bulk_create_entry_db(OrgSuppliers, org_sup_db_list)

        # django_query_instance.django_filter_delete_query(OrgSuppliers, {'guid__in': org_data['delete_supplier']})
        # guid = org_data['supp_org_guid']
        # if guid == '':
        #     guid = guid_generator()
        # defaults = {
        #     'supplier_id': org_data['supp_id'],
        #     'payment_term_key': org_data['payment_term'],
        #     'incoterm_key': django_query_instance.django_get_query(Incoterms, {'incoterm_key': org_data['incoterm']}),
        #     'currency_id': django_query_instance.django_get_query(Currency, {'pk': org_data['currency_id']}),
        #     'ir_gr_ind': org_data['gr_inv_vrf'],
        #     'ir_ind': org_data['inv_conf_exp'],
        #     'gr_ind': org_data['gr_conf_exp'],
        #     'po_resp': org_data['po_resp'],
        #     'ship_notif_exp': org_data['ship_notif_exp'],
        #     'purch_block': org_data['purch_block'],
        #     'porg_id': org_data['porg_id'],
        #     'client_id': getClients(request)
        # }
        # django_query_instance.django_update_or_create_query(OrgSuppliers, {'guid': guid}, defaults)
        supp_org_data = get_data(org_data['supp_id'])
    response = {'supp_org_data': supp_org_data}
    return JsonResponse(supp_org_data, safe=False)


def get_data(supplier_id):
    msgid = 'MSG112'
    message = get_message_desc(msgid)[1]
    upload_response = django_query_instance.django_filter_query(OrgSuppliers,
                                                                {'del_ind': False, 'supplier_id': supplier_id}, None,
                                                                None)
    print(upload_response)
    return upload_response, message


def delete_supplier_org_info(request):
    """
    :param request:
    :return:
    """
    update_user_info(request)
    success_message = ''
    supp_org_data = JsonParser_obj.get_json_from_req(request)
    # supp_org_details = django_query_instance.django_get_query(OrgSuppliers,
    #                                                           {'porg_id': annsmt_data['porg_id']})
    for org_data in supp_org_data['data']:
        if django_query_instance.django_existence_check(OrgSuppliers,
                                                        {'porg_id': org_data['porg_id'],
                                                         'del_ind': False}):
            django_query_instance.django_update_query(OrgSuppliers,
                                                      {'porg_id': org_data['porg_id'],
                                                       'client': global_variables.GLOBAL_CLIENT},
                                                      {'del_ind': org_data['del_ind']})
        supp_org_result = get_supp_org_data(org_data['supp_id'])
    return JsonResponse(supp_org_result, safe=False)


def get_supp_org_data(supplier_id):
    msgid = 'MSG113'
    message = get_message_desc(msgid)[1]
    upload_response = django_query_instance.django_filter_query(OrgSuppliers,
                                                                {'del_ind': False, 'supplier_id': supplier_id}, None,
                                                                None)
    return upload_response, message


def get_supp_org_dropdown(request):
    porg_data = django_query_instance.django_filter_value_list_query(OrgPorg, {
        'client': global_variables.GLOBAL_CLIENT,
        'del_ind': False}, 'porg_id')
    data = {'porg_data': porg_data}
    return JsonResponse(data, safe=False)
