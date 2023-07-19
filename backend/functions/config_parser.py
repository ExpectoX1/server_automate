import configparser
import platform
from subprocess import call


# Ping the host and return the status
def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return call(command) == 0


# getting server details from ini file
def parse_servers(config_file):
    try:
        config = ini_parser(config_file)
        servers = []
        for section in config.sections():
            if section.startswith("server") and "-command" not in section:
                server = {
                    "server_name": section,
                    "host_name": config[section].get("host_name"),
                    "server_loc": config[section].get("location"),
                    "os_version": config[section].get("os_version"),
                    "server_ip": config[section].get("server_ip"),
                    "server_uptime": config[section].get("server_uptime"),
                    "cummi_status": config[section].get("cummi_status"),
                }
                # print(server["server_name"])
                server_address = server["server_ip"]
                if ping(server_address):
                    server["status"] = "Ready"
                else:
                    server["status"] = "Not Ready"
                servers.append(server)
        return servers
    except Exception as e:
        raise Exception(e)


# parsing through the master ini file
def ini_parser(file):
    config = configparser.ConfigParser()
    try:
        result = config.read(file)
        if not result:
            raise Exception(file + " not found")
        return config
    except Exception as e:
        raise Exception(e)
