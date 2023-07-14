# server_automate

<br />Work to do - Backend + Ansible
- Add proper error handling in the parse funtions
- name of ini file is hardcoded => use a search function to check for files ending with ini
- have a function that searches for the path and if it cant find it it throws an error
- After initial ping we can send a list of servers that are down and send this data to ansible commands so that double pinging isnt there [Return a tuple] => decrease time it takes to ping in dead case
- Find a way to standarize the paths everywhere
- any uncaught ansible errors should be display properly check this part => important cause no way to now if the thing failed or not [Parse through the result such that only msg: gets displayed]
- Update + Auto-update
- Check what gets displayed if no result file is present => error gets displayed with no results
=> have frontend handle this case
- If ansible all -m ping says only localhost is found => the config file is probably wrong => exception
- Move all functions from MASTER to BACKEND => only logs
- Ansible playbooks have that file paths are hard coded => change accordingly