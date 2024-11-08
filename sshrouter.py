from netmiko import ConnectHandler

R1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.1',
	'username': 'admin',
	'password': 'pass123',
	'secret': 'cisco'
}

R2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.2',
	'username': 'admin',
	'password': 'pass123',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**R1)
net_connect.enable()

cfg = net_connect.send_config_set(["hostname Router1"])

verify = net_connect.send_command('show running-config | i hostname')
print(verify)

config_commands = [
	'int loopback 1',
	'ip add 10.1.1.1 255.255.255.0',
	'description rawilley loopback',
	]

sendConfig = net_connect.send_config_set(config_commands)
print("{}\n".format(sendConfig))

net_connect.disconnect()


net_connect = ConnectHandler(**R2)
net_connect.enable()

cfg = net_connect.send_config_set(["hostname Router2"])

verify = net_connect.send_command('show running-config | i hostname')
print(verify)

config_commands = [
	'int loopback 1',
	'ip add 172.16.1.1 255.255.255.0',
	'description rawilley on R2',
	]

sendConfig = net_connect.send_config_set(config_commands)
print("{}\n".format(sendConfig))

net_connect.disconnect()
