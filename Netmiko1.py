from netmiko import ConnectHandler

iosv_R1 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.232.134',
  'username': 'vijith',
  'password': 'cisco',
}

iosv_S2 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.232.135',
  'username': 'vijith',
  'password': 'cisco',
}

iosv_S3 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.232.136',
  'username': 'vijith',
  'password': 'cisco',
}

iosv_S4 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.232.137',
  'username': 'vijith',
  'password': 'cisco',
}

with open('iosv_loopback0') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_R1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    output = net_connect.send_command('show ip int brief')
    print (output)

all_devices = [iosv_S2, iosv_S3, iosv_S4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,5):
        print ("Creating VLAN " + str(n))
        config_commands = [' vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)

        output = net_connect.send_command('show vlan brief')
        print (output)
