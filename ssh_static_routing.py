from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = input("Enter your password: ")

R1 = {
    "ip": "192.168.0.104",
    "username":username,
    "password":password,
    "device_type":"cisco_ios"
}

ssh = ConnectHandler(**R1)

print("Connection with Router 1 established successfully..!")

user_input1 = int(input("Enter the number of static routes that you wish to configure: "))

for static in range(0, user_input1):
    nw_id = input("Enter the network id: ")
    mask = input("Enter the network mask: ")
    next_hop = input("Enter the next hop address: ")

    commands = ["ip route "+ nw_id + " " + mask + " " + next_hop]
    static_configs = ssh.send_config_set(commands)
    print(static_configs)

    static_details = ssh.send_command("show run | inc ip route")
    print(static_details)

    ssh.save_config()