# server_automate

<br />Work to do - Backend + Ansible
- Have a function that searches for the ini file and use that name everywhere
- name of ini file is hardcoded => use a search function to check for files ending with ini
- have a function that searches for the path and if it cant find it it throws an error
- After initial ping we can send a list of servers that are down and send this data to ansible commands so that double pinging isnt there [Send array of servers] => decrease time it takes to ping in dead case
- any uncaught ansible errors should be display properly check this part => important cause no way to now if the thing failed or not [Parse through the result such that only msg: gets displayed]
- Update + Auto-update
- Check what gets displayed if no result file is present => error gets displayed with no results
=> have frontend handle this case
- If ansible all -m ping says only localhost is found => the config file is probably wrong => exception
- Ansible playbooks have that file paths are hard coded => change accordingly
- deleting old files in server_result whenever frontend is done
- Implementing os version


Case of file not found
[WARNING]: Unable to parse /home/rithvik_ravilla/server_automate/backend/ansible/inventory/invenory.ini as an
inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'

Case of empty inventory file
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'