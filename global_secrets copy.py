import getpass
import os


def api_get_url():
    return 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def api_username():
    user=os.getenv('USER')
    return user

def api_password():
    passwd = getpass.getpass(api_username()+" Enter your password:")
    return passwd

def api_default_group():
    return "federated-group/XXXXXXXXXXXXXXXXXX"

def grid_endpoint():
    return 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

def s3_access_key():
    access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    return access_key

def s3_secret_key():    
    secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    return secret_key

def tenant_account_for_test():
    tenantid="1111111111111111111"
    return tenantid

def federated_group_for_test():
    federated_group_name="federatedtestgroup"
    return federated_group_name
    