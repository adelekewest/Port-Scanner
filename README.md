# Port-Scanner
A simple script used to scan ports

This script uses the socket module to scan for open ports on a target system. It creates a socket for each port in the specified range and tries to connect to the port using the connect_ex() function. If the connection is successful, the port is considered open and is printed to the console.

To use the script, simply set the target IP address and the port range you want to scan, and run the script. It will scan the ports and print the open ones to the console.
