proto = input("Enter the protocol: ")
platf = input("Enter the platform: ")

if proto == "ssh" and platf == "IOS":
    print("You should use the automation tool Netmiko")
elif proto == "ssh" and platf == "iosxr":
    print("You should use scrapli_netconf")
else:
    print("Unable to support connection")
    