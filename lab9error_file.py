#connections script ssh with Error handling

import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException

USER = input("Enter your login username:  ") 

PASSWORD = getpass ("Enter the password associated with the username: ")


device = { 'ip' : '192.168.80.11' , 'username' : USER, 'password' : PASSWORD, 'device_type' : 'cisco_ios'}

try:
		
		a = ConnectHandler(**device)
except(NetMikoTimeoutException):
		print (f"The attempted connection with the host at the ip address {device['ip']} has been timed out.")
except(NetMikoAuthenticationException):
		print(f"Authentication credentials were incorrect when connecting to the device with the ip address of {device['ip']}. Please try again!")
except(SSHException):
		print(f"You were unable to SSH into the device with ip address {device['ip']} , please try again")


print("Good bye!")

results = a.send_command( 'show running-config')

b = open( 'RouterBackup_05.conf' , 'x')

b.write(results)
b.close()

print(f"You fully have backed up the configuration of the Router at the ip address {device['ip']}")
