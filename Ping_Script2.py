import os


with open("lb.txt") as file:
    hosts = file.read()
    hosts = hosts.splitlines()
    print(" {hosts}  \n")
    # ping for each ip in the file
for ip in hosts:
    response = os.popen(f"ping -c 4 {ip} ").read()
    print(response)

    f = open("ip_output.txt","a")
    f.write(response)
    f.close()
    # creen print is saved in file