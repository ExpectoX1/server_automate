# server_automate
<br />Work to do - Backend + Ansible

1. any uncaught ansible errors should be display properly check this part => important cause no way to know if the thing failed or not [Parse through the result such that only msg: gets displayed]
2. Make a search function that looks for a single ini file in master
3. append the ansible-backup if already found => keep the time at the beginning of each section

- implement ansible vault if possible
- Implementing os version => ansible_facts["distribution"] ?? Kinda difficult to test
