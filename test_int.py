from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter SSH Username: ")
password = getpass("Enter SSH Password: ")

routers = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.196.147",
        "username": username,
        "password": password,
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.196.148",
        "username": username,
        "password": password,
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.196.149",
        "username": username,
        "password": password,
    }
]

commands = [
    "show ip interface brief",
    "show version",
    "show ip route"
]

for router in routers:
    print("\n==============================")
    print(f"Connecting to {router['host']}")
    print("==============================")

    try:
        connection = ConnectHandler(**router)

        for cmd in commands:
            print(f"\nExecuting: {cmd}")
            output = connection.send_command(cmd)
            print(output)

        connection.disconnect()
        print(f"\nDisconnected from {router['host']}")

    except Exception as e:
        print(f"Failed to connect to {router['host']}")
        print(e)
