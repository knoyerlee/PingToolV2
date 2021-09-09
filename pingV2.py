import os

ip_up = []
ip_down = []

# This section takes a txt file formats it and stores it in an array.
file_path = input("Please enter the path to the file you would like to use:\n")

with open(file_path) as f:
    ping_data = f.readline().replace(" ", "\n")

ip_list = ping_data.split("\n")

if "" in ip_list:
    ip_list.remove("")

# This is using the actual ping scan, if a positive response is received do x if not do y.
for ip in ip_list:
    response = os.system("ping -c 5 " + ip)

    if response == 0:
        ip_up.append(ip)
    else:
        ip_down.append(ip)

print("The following addresses returned a positive response:")
for x in ip_up:
    print(x)

print()

print("The following addresses returned a negative response:")
for x in ip_down:
    print(x)