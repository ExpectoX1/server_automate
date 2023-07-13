# server_automate

<br />Work to do - Backend + Ansible
- Send that data to streamlit
- Add proper error handling in the parse funtions
- edge case of naming the result files 'df -H /' final slash becomes a problem apparently => look into it
- any other edge cases take care properly and integrate everything together as menu
- Using app.py run ansible commands in other directories and change accordingly
- pinging using ansible-ping to ensure connection cause this shit kinda bad => get the available servers from here and plan accordingly
- name of ini file is hardcoded => use a search function to check for files ending with ini
- what happens if commands are empty => take care of that case too
- having a {{server}}-command block that isnt used
- Case of all the servers are dead
- Error handling for add_hosts if specific values arent there
