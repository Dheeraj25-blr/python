from netmiko import ConnectHandler
from getpass import getpass

router_ip = open(r"D:\python\routers.txt", "r")

for abc in router_ip:
    print("The Connection is initialized with " + abc)

    username_r = input("Enter your username: ")
    password_r = input("Enter your password: ")

    router_details = {
        "ip":abc,
        "username": username_r,
        "password": password_r,
        "device_type": "cisco_ios"

    }

    ssh = ConnectHandler(**router_details)
    print("SSH Connection was established successfully with " + abc)

    commands_file = open(r'D:\python\commands.txt', 'r')
    output_file = open(r'D:\python\output.txt', 'a')

    for show_command in commands_file:
         details = ssh.send_command(show_command)
         output_file.write("\nThe below information is fetched from " + abc )
         output_file.write("\n" +details + "\n")

# CLOSE AFTER LOOP FINISHES
output_file.close()
commands_file.close()
ssh.disconnect()

print("Output exported successfully.....!")

router_ip.close()

