from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    'ip':'192.168.196.141',
    'username':username,
    'password':password,
    'device_type':'cisco_ios'
}

ssh = ConnectHandler(**router_details)
print("SSH Connection was established successfully..!")

print("Welcome to Router Configuration Utility...!")
user_input = int(input("""Which routing protocol would you like to configure?
                       1. Static Routing
                       2. EIGRP
                       3. OSPF
                       Please make a choice (1/2/3):  """))

if user_input == 1:
    print("You have selected Static Routing.\nPlease Provide the information below to proceed:  ")
    user_input = int(input("Enter the number of static routes that you wish to configure: "))
    for static in range(0, user_input):
        nw_id = input("Enter the network ID: ")
        mask = input("Enter the network mask: ")
        next_hop = input("Enter the next hop address")

        commands = ["ip route " + nw_id + " " + mask + " " + next_hop]
        static_config = ssh.send_config_set(commands)
        print(static_config)

        static_details = ssh.send_command("sh run | inc ip route")
        print(static_details)

elif user_input == 2:
    print("You have selected EIGRP.\nPlease Provide the information below to proceed: ")
    eigrp_as = input("Enter the EIGRP AS Number: ")
    user_input2 = int(input("Enter the number of networks that you wish to add: "))
    for eigrp in range(0, user_input2):
         nw_id = input("Enter the network ID: ")
         wc_mask = input("Enter the wildcard mask: ")

         commands = ["router eigrp " + eigrp_as, "network " + nw_id + " " + wc_mask ]
         eigrp_config = ssh.send_config_set(commands)
         print(eigrp_config)
         eigrp_detail = ssh.send_command("show run | sec eigrp")
         print(eigrp_detail)


elif user_input == 3:
    print("You have selected OSPF Configuration utility/\nPlease Provide te information below to proceed: \n")

    user_input= int(input("Enter the number of networks which you would like to add in OSPF: "))
    OSPF_Process = input("Enter the OSPF Process ID: ")

    for OSPF in range[0, user_input]:
        network_id = input("Enter your network ID: ")
        wildcard_mask = input("Enter the wildcard mask: ")
        area_id = input("Enter the Area ID: ")

        commands = ["router ospf " + OSPF_Process, "network " + network_id + " " + wildcard_mask + "area " + area_id ]
        ospf_config = ssh.send_config_set(commands)
        print(ospf_config)

        ospf_details = ssh.send_command("show run | sec router ospf")
        print(ospf_details)

else:
    print("Invalid input detected.Please Try Again..!")

    ssh.save_config()


                

                                        