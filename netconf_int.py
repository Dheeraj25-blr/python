from ncclient import manager
from getpass import getpass

csr_username = input("Enter the username: ")
csr_password = getpass("Enter the password: ")

router_details = {
    "host":"192.168.196.129",
    "port": 830,
    "username": csr_username,
    "password": csr_password,
    "hostkey_verify":False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection established with the device Successfully..!")

int_payload = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>Loopback2</name>
			<description>Configured using netconfig</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>192.168.2.2</ip>
					<netmask>255.255.255.255</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
    </interfaces>
</config>
"""  

int_conf = netconf.edit_config(int_payload, target = "running")
print(int_conf)

