import subprocess
import sys
import glob, datetime, os, re
import streamlit as st

sys.path.append("../")
from backend.functions.config_parser import ini_parser
from backend.functions.file_checking import valid_path
from backend.functions.log import log_write


# getting ansible output after runnng playbook
# Can be modified to run other commands too
def run_ansible_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            if not result.stderr:
                return result.stdout
            else:
                return result.stderr
        else:
            raise Exception(result.stdout)
    except Exception as e:
        raise Exception(str(e))


# actually running playbook
def ansible_playbook(empty_inventory):
    try:
        log_write("Running Ansible Playbooks")
        if not empty_inventory:
            ansible_command = "ansible-playbook " + valid_path(
                "../backend/ansible/playbooks/execute.yaml"
            )
            run_ansible_command(ansible_command)
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


# doing ansible ping to check if username is right
def ansible_ping():
    try:
        log_write("Pinging The Servers")
        ansible_command = "ansible all -m ping"
        output = run_ansible_command(ansible_command)
        if "[WARNING]:" in output:
            if "Unable to parse" in output:
                # Wrong ini path
                raise Exception("Config Not Found")
            else:
                # Case of empty file
                return True
        return False

    except Exception as output:
        # Config not found
        if "Config Not Found" in str(output):
            raise Exception("INI config file is not found")

        # Finding the servers that ansible cant connect too
        dead_servers = []
        main_file = ini_parser(valid_path("../master/examples.ini"))
        output = str(output).split()
        for i, string in enumerate(output):
            if "UNREACHABLE!" in string:
                if (output[i - 2] + "-command") in main_file.sections():
                    dead_servers.append(output[i - 2])
        dead_servers_str = " ".join(map(str, dead_servers))

        raise Exception(
            dead_servers_str
            + " can not be accessed via ansible. Please check ini credentials"
        )


# setting up ansible inventory file for further use
def ansible_host(servers):
    try:
        log_write("Adding Ansible Hosts")
        # ping failed server list
        dead_server = []
        for server in servers:
            if server["status"] == "Not Ready":
                dead_server.append(server["server_name"])

        main_file = ini_parser(valid_path("../master/examples.ini"))
        with open(valid_path("../backend/ansible/inventory/inventory.ini"), "w+") as f:
            content = f.read()
            for headings in main_file.sections():
                # Exception cases for inventory file
                if "DEFAULT_VAL" in headings:
                    continue
                if "-command" in headings:
                    continue
                if ("group_" + headings) in content:
                    continue
                if headings in dead_server:
                    continue
                else:
                    # Valid server that ansible can connect too
                    if (headings + "-command") in main_file.sections():
                        server_init = "\n[group_" + headings + "]\n" + headings
                        server_host = (
                            " ansible_host=" + main_file[headings]["server_ip"]
                        )
                        server_var = "\n\n[group_" + headings + ":vars]\n"
                        server_user = "ansible_user=" + main_file[headings]["user_name"]

                        # Connection method with either key or password
                        if (
                            "ssh_password" not in main_file[headings]
                            and "ssh_key" not in main_file[headings]
                        ):
                            raise Exception(
                                "Please provide either ssh_password or ssh_key"
                            )
                        if "ssh_password" in main_file[headings]:
                            server_key = (
                                "\nansible_password="
                                + main_file[headings]["ssh_password"]
                                + "\n"
                            )
                        else:
                            server_key = (
                                "\nansible_ssh_private_key_file="
                                + main_file[headings]["ssh_key"]
                                + "\n"
                            )

                        # Writing to the inventory file
                        f.write(
                            server_init
                            + server_host
                            + server_var
                            + server_user
                            + server_key
                        )
    except Exception as e:
        raise Exception(e)


# deleting old result files and creating ansible backup file
# dont use valid path on glob as * will cause not found error
def ansible_backup():
    try:
        read_files = glob.glob("../master/server_out_folder/server*")
        backup_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"

        # Creating backup file
        with open(
            valid_path("../master/logs/ansible_backup/") + backup_name, "a+"
        ) as outfile:
            outfile.write(datetime.datetime.now().strftime("\n%H:%M:%S\n"))
            for f in read_files:
                pattern = r"server\d+"
                match = re.search(pattern, f)
                with open(f, "rb") as infile:
                    outfile.write(match.group() + ":\n" + infile.read().decode() + "\n")

    except Exception as e:
        raise Exception(e)



def delete_ansible():
    try:
        read_files = glob.glob("../master/server_out_folder/server*")
        # Deleting old server_out files
        for f in read_files:
            os.remove(f)
            log_write("Deleted File" + str(f))
    except Exception as e:
        raise Exception(e)


def ansible_backend(servers):
    try:
        log_write("----------Process starts----------")
        ansible_host(servers)
        ansible_playbook(ansible_ping())
        log_write("All Commands Successfully Executed")
        log_write("----------Backend Success----------")
    except Exception as e:
        raise Exception(e)
