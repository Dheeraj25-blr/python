from netmiko import ConnectHandler
from getpass import getpass

router_dictionary = {
   "R1": "192.168.196.142",
   "R2": "192.168.196.143",
   "R3": "192.168.196.144"
}

print(router_dictionary)

user_choice = input("Select the router which you would like to configure (R1/R2/R3): ")
user_choice = user_choice.upper()

router_ip = router_dictionary[user_choice]

router_details = {
        "ip": router_ip,
        "device_type": "cisco_ios",
        "username" : input("Enter your username: "),
        "password" : input("Enter your password: ")
    }

ssh = ConnectHandler(**router_details)
print("The connection was established with " + router_ip)

user_input = int(input("Enter the number of interface that you would like to configure: "))
for interface in range(0, user_input):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface ip: ")
    int_mask = input("Enter the interface mask: ")
    int_desc = input("Enter the interface description: ")

    commands = ["interface " + int_name , "ip address " + int_ip + " " + int_mask, "no shutdown " ]
    int_configs = ssh.send_config_set(commands)
    print(int_configs)

    int_details = ssh.send_command("show ip int brief")
    print(int_details)

    ssh.save_config()

