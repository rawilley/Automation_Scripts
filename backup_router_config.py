from netmiko import ConnectHandler

#First create the device object using a dictionary
R1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.1',
	'username': 'admin',
	'password': 'pass123',
	'secret': 'pass123'
}

#Next establish the SSH connection
net_connect = ConnectHandler(**R1)

#Add new code below
net_connect.enable()
hostname = net_connect.send_command('show running-config | i hostname')
hostname = hostname.split()[-1]
output = net_connect.send_command('show running-config')

filename = f"{hostname}_config_backup.txt"
with open(filename, 'w') as file:
	file.write(output)
	
print(f"{hostname} configuration is saved to {filename}")


#Finally close the connection
net_connect.disconnect()
