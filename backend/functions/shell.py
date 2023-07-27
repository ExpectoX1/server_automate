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
        # print(command)
        # Keeping command as an extra variable for ansible
        playbook_path = valid_path("../backend/ansible/playbooks/shell.yaml")

    # Create the Ansible command using an f-string
        ansible_command = f"ansible-playbook {playbook_path} --extra-vars \"shell_command='{command}'\""
        # print(ansible_command)
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
        st.error(error_message.strip())
