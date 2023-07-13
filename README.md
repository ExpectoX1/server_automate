# server_automate

<br />Work to do - Backend + Ansible
- Add proper error handling in the parse funtions
- edge case of naming the result files 'df -H /' final slash becomes a problem apparently => look into it
- Using app.py run ansible commands in other directories and change accordingly
- name of ini file is hardcoded => use a search function to check for files ending with ini
- have a function that searches for the path and if it cant find it it throws an error
- After initial ping we can send a list of servers that are down and send this data to ansible commands so that double pinging isnt there [Return a tuple ]
- Find a way to standarize the paths everywhere
- any uncaught ansible errors should be display properly check this part
- Update + Auto-update