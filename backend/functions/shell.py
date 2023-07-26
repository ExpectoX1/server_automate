import sys
import glob, os
import streamlit as st

sys.path.append("../")
from backend.functions.file_checking import valid_path
from backend.functions.log import log_write
from backend.functions.ansible import run_ansible_command

def ansible_shell(command):
    try:
        read_files = glob.glob("../master/shell_out_folder/s*")
        # Deleting old server_out files
        for f in read_files:
            os.remove(f)
            log_write("Deleted File" + str(f))
        
        log_write("Running Ansible Shell playbook")
        #Keeping command as an extra variable for ansible
        ansible_command = 'ansible-playbook ' + valid_path(
            '../backend/ansible/playbooks/shell.yaml'
        ) + ' --extra-vars "shell_command=' + command + '"'
        run_ansible_command(ansible_command)
        log_write("Ansible Shell Command Successfully Executed")

    except Exception as e:
        #Parsing ansible playbook output for all error messages
        error = str(e).split()
        error_message = ""
        for indx, string in enumerate(error):
            if '"msg":' in string:
                while "}" not in error[indx]:
                    error_message += error[indx] + " "
                    indx += 1
            error_message += "\n"
        log_write(error_message.strip())
        st.toast(error_message.strip())