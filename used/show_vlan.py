from netmiko import (ConnectHandler)

exos_hosts = ["10.10.1.31", '10.10.1.22', '10.10.1.30', '10.10.1.32']

index = 0
for host in exos_hosts:
	
	switch = {
	'host': exos_hosts[index], 
	'port': '22', 
	'username': 'admin', 
	'password': '',
	'device_type': 'extreme_exos'}

	connection = ConnectHandler(**switch)
	show_vlan = connection.send_command('show vlan | grep VR')
	print(show_vlan)

	connection.disconnect()
	index += 1
