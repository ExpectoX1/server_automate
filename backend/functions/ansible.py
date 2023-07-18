import subprocess
import sys
#ansible backup
import glob,datetime,os,re
sys.path.append("../")
from backend.functions.config_parser import ini_parser
from backend.functions.file_checking import valid_path

#getting ansible output after runnng playbook
def run_ansible_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True ,shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            raise Exception(result.stdout)
    except Exception as e:
        raise Exception(str(e))

#actually running playbook
def ansible_playbook():
    ansible_command = "ansible-playbook " + valid_path("../backend/ansible/playbooks/execute.yaml")
    try:
        output = run_ansible_command(ansible_command)
        return output
    except Exception as e:
        raise Exception(e)

#doing ansible ping to check if username is right
def ansible_ping():
    try:
        ansible_command = "ansible all -m ping"
        output = run_ansible_command(ansible_command)        
    except Exception as output:
        dead_servers = []
        main_file = ini_parser(valid_path("../master/examples.ini"))
        output = str(output).split()
        for i, string in enumerate(output):
            if "UNREACHABLE!" in string:
                if (output[i-2] + "-command") in main_file.sections(): 
                    dead_servers.append(output[i-2])
        dead_servers_str = ' '.join(map(str, dead_servers))
        raise Exception(dead_servers_str + " can not be accessed via ansible. Please check username / key path")

#setting up ansible inventory file for further use
def ansible_host():
    try:
        main_file = ini_parser("../master/examples.ini")
        #Error handling for the file search too
        with open('../backend/ansible/inventory/inventory.ini','w+') as f:
            content = f.read()
            for headings in main_file.sections():
                if ("-command" in headings):
                    continue
                if ("group_" + headings) in content:
                    continue
                else:
                    if (headings + "-command") in main_file.sections():
                        server_init = "\n[group_"+ headings+ "]\n" + headings
                        server_host = " ansible_host="+ main_file[headings]["server_ip"]
                        server_var = "\n\n[group_"+ headings+ ":vars]\n"
                        server_user = "ansible_user=" +  main_file[headings]["user_name"]
                        server_key = "\nansible_ssh_private_key_file=" + main_file[headings]["key_path"] + "\n"
                        f.write(server_init + server_host + server_var + server_user + server_key)
    except Exception as e:
        raise Exception(e)

#deleting old result files and creating ansible backup file
def ansible_backup():
    read_files = glob.glob("../master/server_out_folder/server*")
    backup_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    with open(valid_path("../master/logs/ansible_backup/") + backup_name, "wb+") as outfile:
        for f in read_files:
            pattern = r'server\d+'
            match = re.search(pattern,f)
            with open(f, "rb") as infile:
                outfile.write(match.group().encode('utf-8') + "\n".encode('utf-8') + infile.read() + "\n".encode('utf-8'))
    for f in read_files:
        os.remove(f)