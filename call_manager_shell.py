#!/bin/python3.6
import getpass
import paramiko
import threading
from paramiko_expect import SSHClientInteraction


USERNAME = input('Enter device username: ')
PASSWORD = getpass.getpass('Enter Pass: ')

with open('ip_list.txt', mode='rt', encoding='utf-8') as f:
    ip_addr = [line.rstrip('\n') for line in f]


for i in ip_addr:
    print(i)
    device_connect = [i, USERNAME, PASSWORD]
    device_connections.append(device_connect)

def session(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(ip, username=username, password=password)
        interact = SSHClientInteraction(ssh, timeout=90, display=True)

        interact.expect('admin:')
        interact.send('show risdb query phone')
        interact.expect('admin:')
        output = interact.current_output_clean
    finally:
        ssh.close()


    ip_file_name = ip.replace('.','_')
    output_file = '{}.csv'.format(ip_file_name)
    with open(output_file, mode='wt', encoding='utf-8') as out:
        out.write(output)

for i in device_connections:
	t = threading.Thread(target = session(i[0], i[1], i[2]))
	t.daemon = True
	t.start()
