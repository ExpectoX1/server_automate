# server_automate

<br />Work to do - Backend + Ansible

- have a function that searches for the path and if it cant find it it throws an error => to be used by all functions with file paths

3. After initial ping we can send a list of servers that are down and send this data to ansible commands so that double dead pinging isn't there [Send array of servers]

1. Deleting server_out files and creating a backup

2. Creating empty files for servers that are not running anything either

- any uncaught ansible errors should be display properly check this part => important cause no way to now if the thing failed or not [Parse through the result such that only msg: gets displayed]

- Update + Auto-update
- Check what gets displayed if no result file is present => error gets displayed with no results
=> have frontend handle this case
5.  If ansible all -m ping says only localhost is found => the config file is probably wrong => exception
4. Implementing os version

Case of file not found
[WARNING]: Unable to parse /home/rithvik_ravilla/server_automate/backend/ansible/inventory/invenory.ini as an
inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'

Case of empty inventory file
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'