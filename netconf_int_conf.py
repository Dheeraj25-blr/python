from ncclient import manager
from getpass import getpass

csr_username = input("Enter the username: ")
csr_password = getpass("Enter the password: ")

router_details = {
    "host":"192.168.196.129",
    "port": 830,
    "username": csr_username,
    "password": csr_password,
    "hostkey_verify":False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection established with the device Successfully..!")

user_input = int(input("Enter the number of interfaces that you wish to configure: "))

for int_conf in range(0, user_input):

    user_choice = int(input("Enter the type of interface that you wish to configure:\n1. Physical Interface\n2. Loopback Interface\nPlease make a choice: "))

    if user_choice == 1:
        int_type = "ethernetCsmacd"
    elif user_choice == 2:
        int_type = "softwareLoopback"
    else:
        break
    int_name = input("Enter your interface name: ")
    int_ip = input("Enter your interface IP address: ")
    int_mask = input("Enter your interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

    int_payload = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{int_name}</name>
                <description>{int_desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{int_type}</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{int_ip}</ip>
                        <netmask>{int_mask}</netmask>
                    </address>
                </ipv4>
                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
            </interface>
        </interfaces>
    </config>
    """  

    int_conf = netconf.edit_config(int_payload, target = "running")
    print(int_conf)



