import bluetooth

# Define the MAC address of the Bluetooth device you want to communicate with
target_address = '00:5B:94:06:47:3E'  # Replace with your device's MAC address

# Define the message you want to send
message = "Hello, this is a prompt from Python!"

# Try to connect to the Bluetooth device
try:
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((target_address, 1))  # RFCOMM channel 1 is commonly used

    # Send the message
    socket.send(message)

    # Close the connection
    socket.close()
    print("Message sent successfully!")

except Exception as e:
    print("Error:", e)

