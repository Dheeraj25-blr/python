from netmiko import ConnectHandler

router_username = input("Enter your username: ")
router_password = input("Enter your password: ")

router_details = {
    "ip" :"192.168.0.104",
    'username': router_username,
    'password': router_password,
    "device_type":"cisco_ios"
}

ssh = ConnectHandler(**router_details)

print("Connection with Router 1 established successfully..!")
print("The Current state of the interface is as follow: ")

int_details = ssh.send_command("show ip interface brief")
print(int_details)

int_name= input("Enter the interface name: ")
int_ip = input("Enter the interface IP address: ")
int_mask= input("Enter the interface subnet mask: ")
int_desc = input("Enter the interface description:")

commands = [f'interface {int_name}', 'ip address {} {}'.format(int_ip, int_mask), 'desc ' + int_desc , 'no shutdown']
int_configs = ssh.send_config_set(commands)
print(int_configs)

updated_int_details = ssh.send_command(input("Enter the show command that you wish to run"))
print(updated_int_details)

ssh.save_config()

ssh.disconnect()