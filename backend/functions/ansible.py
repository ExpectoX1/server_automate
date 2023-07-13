import platform
import subprocess

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
    for i, string in enumerate(output):
        if "UNREACHABLE!" in string:
            dead_servers.append(output[i-2])
    print(dead_servers)
    