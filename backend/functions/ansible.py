import subprocess
import sys
sys.path.append('../')
from MASTER.config_parser import ini_parser

def run_ansible_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True ,shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stdout
    except Exception as e:
        raise Exception(str(e))

def ansible_playbook():
    #error handling in case it cant find the playbook
    ansible_command = "ansible-playbook" +" ansible/playbooks/execute.yaml"
    try:
        output = run_ansible_command(ansible_command)
        return output
    except Exception as e:
        raise Exception(e)


def ansible_ping():
    ansible_command = "ansible all -m ping"
    output = run_ansible_command(ansible_command).split()
    dead_servers = []
    main_file = ini_parser("../MASTER/examples.ini")
    for i, string in enumerate(output):
        if "UNREACHABLE!" in string:
            if (output[i-2] + "-command") in main_file.sections(): 
                dead_servers.append(output[i-2])
    if dead_servers:
        dead_servers_str = ' '.join(map(str, dead_servers))
        raise Exception(dead_servers_str + " can not be accessed via ansible. Please check username / key path")
        # print(dead_servers_str + " can not be accessed via ansible. Please check username / key path")    