import sys
sys.path.append('../')
from MASTER.config_parser import ini_parser
from functions.ansible import ansible_ping

def add_host():
    try:
        main_file = ini_parser("../MASTER/examples.ini")
        #Error handling for the file search too
        with open('ansible/inventory/inventory.ini','w+') as f:
            content = f.read()
            #edge cases when you have shit like server12 followed by server1
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