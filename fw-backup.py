from netmiko import ConnectHandler
import datetime

fgt= {
    'host': 'Lab-Forti-1',
    'device_type': 'fortinet',
    'ip': '192.168.1.36',
    'username': 'admin',
    'password': 'Thenry14'
}

net_connect = ConnectHandler(**fgt)
comment = 'Connecting to Device'
print(comment)

# run configuration output on device
output = net_connect.send_command('sh full-configuration')

# file formatting
current_time = datetime.datetime.today().strftime('%Y_%b_%d')

# Create file with formatting and full configuration backup
with open ('/home/msmith/fw_backups/' + str(fgt ['host']) + '_' + str(current_time) + '.cfg' , 'w') as f:
    for line in output:
        f.write(line)

print('backup  Complete')
net_connect.disconnect()


