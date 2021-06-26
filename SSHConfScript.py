#connections script ssh

import os
from netmiko import ConnectHandler
from getpass import getpass

USER = input("Enter your login username:  ") 

PASSWORD = getpass ("Enter the password associated with the username: ")


device = { 'ip' : '192.168.80.11' , 'username' : USER, 'password' : PASSWORD, 'device_type' : 'cisco_ios'}


a = ConnectHandler(**device)

results = a.send_command( 'show running-config')

b = open( 'R1config.conf' , 'x')

b.write(results)
b.close()

