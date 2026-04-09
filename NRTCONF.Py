from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")

router_details = {
    'host' : '192.168.196.129',
    'username' : csr_username,
    'password' : csr_password,
    'port' : '830',
    'hostkey_verify' : False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection was Created successfully...!")

running_conf = netconf.get_config(source = "running")
print(running_conf)

running_conf = netconf.get_config(source = "running")
pretty_running_conf = parseString(running_conf.xml).toprettyxml()
print(pretty_running_conf)

myfile = open(r"D:\python\output.txt", "w")
myfile.write(pretty_running_conf)

print("Configurations exported successfully...!")

