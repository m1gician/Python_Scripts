from netmiko import ConnectHandler
from getpass import getpass
import datetime

#Promt for username and password
username = input('Enter your remote username: ')
password = getpass()

asa = {
    'host': 'ashp-vp2',
    'device_type': 'cisco_asa',
    'ip': '10.2.247.250',
    'username': username,
    'password': password
}

net_connect = ConnectHandler(**asa)
comment = 'Connecting to Firewall'
print(comment)

# run configuration output on device
output = net_connect.send_command('show running-config')

# file formatting
current_time = datetime.datetime.today().strftime('%Y_%b_%d')

# Create file with formatting and full configuration backup
with open ('/home/msmith/fw_backups/' + str(asa ['host']) + '_' + str(current_time) + '.cfg' , 'w') as f:
    for line in output:
        f.write(line)

print('Backup  Complete')
net_connect.disconnect()


