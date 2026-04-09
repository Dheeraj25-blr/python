from netmiko import ConnectHandler
from getpass import getpass

r_username = input("Enter your username: ")
r_password = input("Enter your password: ")

router_details = {
    'ip': '192.168.0.104',
    'username':r_username,
    'password':r_password,
    "device_type":"cisco_ios",

}

ssh = ConnectHandler(**router_details)
print("SSH Connection created successfully..!")

user_input = int(input("Enter the number of interface that you wish to configure:"))

for int_conf in range(0, user_input):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface mask: ")
    int_desc = input("Enter the interface description: ")

    commands = ["interface " + int_name, "ip address " + int_ip + " " + int_mask, "desc " + int_desc, "no shutdown"]
    int_conf = ssh.send_config_set(commands)
    print(int_conf)

    int_details = ssh.send_command("Show ip interface br")
    print(int_details)

    ssh.save_config()
    