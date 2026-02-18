import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
from payload import csr_int_conf
 
asav = "192.168.196.130"
csrv = "192.168.196.129"
 
user_choice = int(input("""Welcome to the Network Configuration Utility.
What would you like to configure:
1. CSR1Kv
2. ASAv
Please make a choice (1/2): """))
 
if user_choice == 1:
    print("You have selected CSR\nPlease provide the information below to proceed: ")
 
    csr_username = input("Enter your username: ")
    csr_password = getpass("Enter your password: ")
 
    r_url = f"https://{csrv}/restconf/data/ietf-interfaces:interfaces"
 
    r_creds = HTTPBasicAuth(username = csr_username, password = csr_password)
 
    r_headers = {"Content-Type":"application/yang-data+json"}
 
    csr_int_conf(csr_url = r_url, csr_creds = r_creds, csr_headers = r_headers)
 