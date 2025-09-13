from netmiko import (ConnectHandler)

targets = [
	{'host': '10.10.1.30', 'name': 'IT_Network',   'vid': 100},
	{'host': '10.10.1.31', 'name': 'MGMT_Network', 'vid': 200},
	{'host': '10.10.1.32', 'name': 'ACCT_Network', 'vid': 300},
	{'host': '10.10.1.22', 'name': 'USER_Network', 'vid': 400}]
	
common = {
	'device_type': 'extreme_exos',
	'username': 'admin',
	'password': ''}
	
for target in targets:
	connection = ConnectHandler(host=target['host'], **common)
	command = f"configure vlan {target['name']} tag {target['vid']}"
	connection.send_command(command)
	connection.send_command('save configuration')
	print(f"{target['host']}: {command}")
	print(f"{target['host']}: save configuration")
	connection.disconnect()		
