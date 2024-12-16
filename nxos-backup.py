from netmiko import ConnectHandler
import datetime

nxos= {
    'host': 'nbp-cor-sw1',
    'device_type': 'cisco_nxos',
    'ip': '10.20.249.1',
    'username': 
    'password': 
}

net_connect = ConnectHandler(**nxos)
comment = 'Connecting to Device'
print(comment)

# run configuration output on device
output = net_connect.send_command('show running-config')

# file formatting
current_time = datetime.datetime.today().strftime('%Y_%b_%d')

# Create file with formatting and full configuration backup
with open ('/home/msmith/fw_backups/' + str(nxos ['host']) + '_' + str(current_time) + '.cfg' , 'w') as f:
    for line in output:
        f.write(line)

print('Backup  Complete')
net_connect.disconnect()


