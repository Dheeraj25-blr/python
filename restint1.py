import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
from payl import csr_int_conf, asa_int_conf

asav = "192.168.196.130"
csrv = "192.168.196.129"

while True:
    user_choice = input("""Welcome to the Network Configuration Utility.
    What would you like to configure: 
    1. CSR1Kv
    2. ASAv
    Please make a choice (1/2): """)

    if user_choice in ('1', '2'):
        break
    else:
        print("Invalid Selection. Try again..!")

if user_choice == '1':
    print("You have selected CSR\nPlease provide the information below to proceed: ")

    csr_username = input("Enter your username: ")
    csr_password = getpass("Enter your password: ")

    r_url = f"https://{csrv}/restconf/data/ietf-interfaces:interfaces"

    r_creds = HTTPBasicAuth(username = csr_username, password = csr_password)

    r_headers = {"Content-Type":"application/yang-data+json"}

    csr_int_conf(csr_url = r_url, csr_creds = r_creds, csr_headers = r_headers)

elif user_choice == "2":
    print("You have selected ASA\nPlease provide the information below to proceed:") 

    asa_username = input("Enter your username: ")
    asa_password = getpass("Enter your password: ")

    object_id = input("Enter the interface Object ID (for eg. GigabitEthernet0_API_SLASH_0 for Gig0/0): ")

    fw_url = f"https://{asav}/api/interfaces/physical/{object_id}"
    fw_creds = HTTPBasicAuth(username = asa_username, password = asa_password)

    fw_headers = {"Content-Type":"application/json"}

    asa_int_conf(asa_url = fw_url, asa_creds=fw_creds, asa_headers=fw_headers)

else:
    print("Invalid Input. Try again!!")