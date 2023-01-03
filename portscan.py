import socket

# Set the target IP address and port range
ip_address = "192.168.1.100"
start_port = 1
end_port = 65535

# Scan the ports
for port in range(start_port, end_port+1):
  # Create a socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Set the timeout to 1 second
  s.settimeout(1)

  # Try to connect to the port
  result = s.connect_ex((ip_address, port))

  # Check the result
  if result == 0:
    print("Port {} is open".format(port))
  s.close()
