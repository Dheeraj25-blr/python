from netmiko import ConnectHandler

router_details = {
    'ip': '192.168.196.135',
    'username': 'admin',
    'password' : 'cisco',
    'device_type': 'cisco_ios'
}

ssh = ConnectHandler(**router_details)
print("SSH Connection was created successfully with the device..!!!")

commands = ['interface loopback 0', 'ip address 192.168.0.1 255.255.255.0', 'desc Configured using NETMIKO']

int_configs = ssh.send_config_set(commands)
print(int_configs)

int_details = ssh.send_command("show ip int brief")
print(int_details)

ssh.save_config()

ssh.disconnect