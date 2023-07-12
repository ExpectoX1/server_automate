import configparser

def parser():
    #Creaing outermost json
    json_dict = {}
    config = configparser.ConfigParser()
    #Reading file
    config.read("examples.ini")
    for headings in config.sections():
        #Server Json Object
        json_dict[headings] = {}
        server_address = ""
        print(headings)
        for sub in config[headings]:
                #Filling up server object
                if sub == "user_name":
                    json_dict[headings][sub] = config[headings][sub]
                if sub == "host_name":
                    json_dict[headings][sub] = config[headings][sub]
                if sub == "server_ip":
                    server_address += config[headings][sub]
                    json_dict[headings][sub] = config[headings][sub]
        #Status check by ping
        # check = ping(server_address)
        # if check == 1:
        #     json_dict[headings]["status"] = "Server Reachable"
        # else:
        #      json_dict[headings]["status"] = "Server is not reachable"
    return json_dict

# def run_ansible_ping():
# 	ansible_command = "ansible all -m ping"
# 	output = run_ansible_command(ansible_command)