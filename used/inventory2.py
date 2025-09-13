import configparser
config = configparser.ConfigParser()
config.optionxform = str ## Keeps the original case letters. Doesn't lowercase everything ## 					

template = {
	'RAM': '512MB',
	'vCPUs': '1',
	'Qemu binary': '/usr/bin/qemu-system-x86-64(v4.2.1)',
	'Boot priority': 'CD/DVD-ROM or HDD',
	'On close': 'Power off the VM',
	'Console type': 'telnet',
	'Adapters': '13',
	'Type': 'Realtek 8139 Ethernet (rtl8139)',
	'Replicate network connection states in Qemu': 'Yes'}
	
switches = [
	{'section': 'IT',   'Name':   'IT-Network', 'Base MAC': '0c:1c:b2:85:00:00'},
	{'section': 'MGMT', 'Name': 'MGMT-Network', 'Base MAC': '0c:cc:78:5d:00:00'},
	{'section': 'ACCT', 'Name': 'ACCT-Network', 'Base MAC': '0c:1c:b2:86:00:00'},
	{'section': 'USER', 'Name': 'USER-Network', 'Base MAC': '0c:cc:78:5e:00:00'}]
	
for dept in switches:
	section = dept.pop('section')
	config[section] = {**template, **dept}		
	
with open('inventory2.ini', 'w') as file:
	config.write(file)	
