# server_automate
<br />Work to do - Backend + Ansible

1. After initial ping we can send a list of servers that are down and send this data to ansible commands so that double dead pinging isn't there [Send array of servers]

- any uncaught ansible errors should be display properly check this part => important cause no way to now if the thing failed or not [Parse through the result such that only msg: gets displayed]

- Update + Auto-update
3.  If ansible all -m ping says only localhost is found => the config file is probably wrong
=> exception (Does the same thing happen if we have empty inventory)
2. Implementing os version
- Make a search function that looks for an ini file in master


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
Ansible
configparser
schedule
streamlit