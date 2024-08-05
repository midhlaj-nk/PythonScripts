import bluetooth as bt



nearby_devices = bt.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

x = int(1)
bluetooth_devices = []
for addr, name in nearby_devices:
    new_device = ("{} - Address: {} - Name: {}").format(x, addr, name)
    bluetooth_devices.append(new_device)
    x += 1
    print(new_device + "\n")


#print(bluetooth_devices)
device_number = int(input("\nWhich bluetooth device do you want to connect to? (enter number) ")) -     1

print(bluetooth_devices[device_number])
device = bluetooth_devices[device_number]

y = 13
z = 30

if device_number > 9 < 100:
    y += 1
    z += 1
address = str(device)[y:z]


print(address)