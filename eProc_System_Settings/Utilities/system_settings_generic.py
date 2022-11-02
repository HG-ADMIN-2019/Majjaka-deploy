"""Copyright (c) 2020 Hiranya Garbha, Inc.
Name:
    system_settings_specific.py
Usage:
   saves the system settings from UI
     sys_attributes: gets the respective attribute values for the logged in client and used to integrate them n respective functionality.
Author:
    Soni Vydyula
"""
from eProc_Basic.Utilities.functions.django_query_set import DjangoQueries
from eProc_Configuration.models import  SystemSettingsConfig

django_query_instance = DjangoQueries()


class sys_attributes:
    def __init__(self, client):
        self.client = client
        self.sys_attr = django_query_instance.django_filter_only_query(SystemSettingsConfig,
                                                                       {'client': client}).values()

    # Gets the login attempt for logged in client
    def get_login_attempts(self):
        login_attempts =0
        if self.sys_attr:
            sys_attribute = 'LOGIN_ATTEMPTS'
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                if attr.sys_attr_value == '' or attr.sys_attr_value is None:
                    login_attempts = 0
                else:
                    login_attempts = attr.sys_attr_value
        return login_attempts

    # Gets the password policy
    def get_pwd_policy(self):
        if self.sys_attr:
            sys_attribute = 'PWD_POLICY'
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                password = attr.sys_attr_value
                pwd_policy = password.split("_")
            return pwd_policy

    def get_attachment_extension(self):
        if self.sys_attr:
            sys_attribute = 'ATTACHMENT_EXTENSION'
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                attachment_extension = attr.sys_attr_value
                attachment_extension_value = attachment_extension.split("_")
            return attachment_extension_value

    def get_attachment_size(self):
        if self.sys_attr:
            sys_attribute = 'ATTACHMENT_SIZE'
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                attachment_size = attr.sys_attr_value
            return attachment_size

    def get_acct_assignment_category(self):
        if self.sys_attr:
            sys_attribute = 'ACCOUNT_ASSIGNMENT_CATEGORY'
            acct_assignment_category = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                acct_assignment_category = attr.sys_attr_value
            return acct_assignment_category

    def get_purchase_group(self):
        if self.sys_attr:
            sys_attribute = 'PURCHASE_GROUPS'
            purchase_groups = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                purchase_groups = attr.sys_attr_value
            return purchase_groups

    def get_edit_address(self):
        if self.sys_attr:
            sys_attribute = 'EDIT_ADDRESS'
            edit_address = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                edit_address = attr.sys_attr_value
            return edit_address

    def get_frequently_purchased(self):
        if self.sys_attr:
            sys_attribute = 'FREQUENTLY_PURCHASED_ITEMS'
            frequently_purchased = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                frequently_purchased = attr.sys_attr_value
            return frequently_purchased

    def get_recently_viewed(self):
        if self.sys_attr:
            sys_attribute = 'RECENTLY_VIEWED_ITEMS'
            recently_viewed = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                recently_viewed = attr.sys_attr_value
            return recently_viewed

    def get_shipping_address(self):
        if self.sys_attr:
            sys_attribute = 'CHANGE_SHIPPING_ADDRESS'
            shipping_address = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                shipping_address = attr.sys_attr_value
            return shipping_address

    def get_limit_item(self):
        if self.sys_attr:
            sys_attribute = 'LIMIT_ITEM'
            limit_item = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                limit_item = attr.sys_attr_value
            return limit_item

    def get_add_favourites(self):
        if self.sys_attr:
            sys_attribute = 'ADD_TO_FAVOURITES'
            add_favourites = ''
            attributes = self.get_system_settings_list(sys_attribute)
            for attr in attributes:
                add_favourites = attr.sys_attr_value
            return add_favourites

    def get_system_settings_list(self, sys_attr_type):
        attributes = django_query_instance.django_filter_only_query(SystemSettingsConfig, {
            'client': self.client, 'del_ind': False, 'sys_attr_type': sys_attr_type,
            'sys_settings_default_flag': True})
        return attributes
