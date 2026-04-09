from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter username: ")
password = getpass("Enter password: ")

# Router details in list (Loop will handle all)
routers = [
    {"ip": "192.168.57.129", "loopback": "1.1.1.1"},
    {"ip": "10.10.10.2", "loopback": "2.2.2.2"},
    {"ip": "20.20.20.2", "loopback": "3.3.3.3"}
]

for router in routers:

    device = {
        "device_type": "cisco_ios",
        "ip": router["ip"],
        "username": username,
        "password": password
    }

    print(f"\nConnecting to Router {router['ip']}...")

    try:
        ssh = ConnectHandler(**device)
        print("SSH Connected Successfully")

        # Loopback configuration commands
        config_commands = [
            "interface loopback0",
            f"ip address {router['loopback']} 255.255.255.255",
            "no shutdown"
        ]

        output = ssh.send_config_set(config_commands)
        print(output)

        # Save configuration
        ssh.save_config()
        print("Configuration Saved Successfully")

        ssh.disconnect()

    except Exception as e:
        print(f"Error connecting to {router['ip']}: {e}")

print("\nAll routers configured successfully!")