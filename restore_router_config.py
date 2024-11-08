from netmiko import ConnectHandler

#First create the device object using a dictionary
R1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.1',
	'username': 'admin',
	'password': 'pass123',
	'secret': 'pass123'
}

#Part 1 Add New code below.
backup_file = input("Enter the name of the backup file to restore: ")

with open (backup_file, 'r') as file:
	backup_config = file.read()

#Next establish the SSH connection
net_connect = ConnectHandler(**R1)


#Part 2 add new code below.
net_connect.enable()
net_connect.config_mode()

output = net_connect.send_command_timing(backup_config)

print("Configuration restored")

net_connect.exit_config_mode()

#Finally close the connection
net_connect.disconnect()
