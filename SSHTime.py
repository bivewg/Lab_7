#connections script ssh

import os
from netmiko import ConnectHandler
from getpass import getpass
import datetime

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)



USER = input("Enter your login username:  ") 

PASSWORD = getpass ("Enter the password associated with the username: ")


device = { 'ip' : '192.168.80.11' , 'username' : USER, 'password' : PASSWORD, 'device_type' : 'cisco_ios'}


a = ConnectHandler(**device)

results = a.send_command( 'show running-config')

file_name =  current_date_and_time_string + '2R1config.conf' 
b = open( file_name , 'x')

b.write(results)
b.close()

