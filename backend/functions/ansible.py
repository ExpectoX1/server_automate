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
        return str(e)

def ansible_playbook():
    #error handling in case it cant find the playbook
    ansible_command = "ansible-playbook" +" backend/ansible/playbooks/execute.yaml"
    output = run_ansible_command(ansible_command)
    return output


def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0