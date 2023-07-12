import configparser

#add some error handling here itself so it doesnt become a problem later
#error handling doesnt feel right
# Look for alternate methods to pass error around
def ini_parser():
    config = configparser.ConfigParser()
    try:
        config.read("examples.ini")
    except Exception as e: 
        # error_pass(e)
        return 0
    return config

def add_host():
    
    #Respond and handle the error accordingly
    main_file = ini_parser()
    if main_file == 0:
        return "Cant add hosts due to duplicate sections"    
    
    #Error handling for the file search too
    with open('ansible/inventory/inventory.ini','w+') as f:
        content = f.read()
        #edge cased when you have shit like server12 followed by server1
        for headings in main_file.sections():
            if ("-command" in headings):
                continue
            if ("group_" + headings) in content:
                continue
            # put error handling for cases when inventory file and specific fields are not in example
            # put it with ini parser cause problems could occur
            else:
                server_init = "\n[group_"+ headings+ "]\n" + headings
                server_host = " ansible_host="+ main_file[headings]["server_ip"]
                server_var = "\n\n[group_"+ headings+ ":vars]\n"
                server_user = "ansible_user=" +  main_file[headings]["user_name"]
                server_key = "\nansible_ssh_private_key_file=" + main_file[headings]["key_path"] + "\n"
                f.write(server_init + server_host + server_var + server_user + server_key)
    return "Test"