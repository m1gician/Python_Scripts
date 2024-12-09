from netmiko import ConnectHandler


#This script is used to connect to multiple fotigate hosts in a file
#Then run show commands


with open('device_file') as f:
    device_list = f.read().splitlines()

for devices in device_list:
    print ('Connecting to device ' + devices)
    ip_address_of_device = devices
    fgt = {
    'device_type': 'fortinet',
    'ip': ip_address_of_device,
    'username': 'admin',
    'password': 'Thenry14'
}

net_connect = ConnectHandler(**fgt)

# run configuration output
output = net_connect.send_command('get system status')
print(output)
