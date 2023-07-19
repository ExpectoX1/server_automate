# server_automate
<br />Work to do - Backend + Ansible

2. After initial ping we can send a list of servers that are down and send this data to ansible commands so that double dead pinging isn't there [Send array of servers]
6. any uncaught ansible errors should be display properly check this part => important cause no way to now if the thing failed or not [Parse through the result such that only msg: gets displayed]
1. bug: create dead files is removing data
-  Implementing os version
7. append the ansible-backup if already found => keep the time at the beginning of each section
5. Make a search function that looks for an ini file in master
3. During ini_parser check for all the important configs => throw error if not found
[Cant have both password and key => keep that
=> try to implement ansible vault if possible]

4.  If ansible all -m ping says only localhost is found => the config file is probably wrong
=> exception (Does the same thing happen if we have empty inventory => check if commands is there and if not then we can throw an error => ansible_playbook should not run in that case)

Case of file not found
[WARNING]: Unable to parse /home/rithvik_ravilla/server_automate/backend/ansible/inventory/invenory.ini as an
inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'

Case of empty inventory file
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'

Installation:

Pip:
Ansible
configparser
schedule
streamlit

Linux Installation
sshpass for password case => apt-get install

note: to use ansible with password you must once ssh into server and add fingerprint