import configparser
import platform
from subprocess import call, DEVNULL


# Ping the host and return the status
def ping(host):
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        return call(command, stdout=DEVNULL, stderr=DEVNULL) == 0
    except Exception as e:
        raise Exception(e)


# getting server details from ini file
def parse_servers(config_file):
    try:
        config = ini_parser(config_file)
        servers = []
        refresh = None
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
                # Checking for server connection with ping
                server_address = server["server_ip"]
                if ping(server_address):
                    server["status"] = "Ready"
                else:
                    server["status"] = "Not Ready"
                servers.append(server)
            if section.startswith("DEFAULT_VAL"):
                refresh = config[section].get("refresh_time")

        return servers, refresh
    except Exception as e:
        raise Exception(e)


# parsing through the master ini file
def ini_parser(file):
    try:
        config = configparser.ConfigParser()
        result = config.read(file)
        if not result:
            raise Exception(file + " not found")
        return config
    except Exception as e:
        raise Exception(e)
