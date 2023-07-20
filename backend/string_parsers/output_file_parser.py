import sys

sys.path.append("../string_parsers/")
from uptime_parser import extract_uptime_value
from mem_parser import extract_percentage_value
from version_parser import extract_os_version
import os
import re


def generate_array():
    def extract_text_files(folder_path):
        text_files = []

        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a text file
            if os.path.isfile(file_path) and file_name.lower().endswith(".txt"):
                text_files.append(file_path)

        return text_files

    def extract_values_from_text(file_path):
        with open(file_path, "r") as file:
            text = file.read()
            uptime = extract_uptime_value(text)
            mem_percentage = extract_percentage_value(text)
            os_version = extract_os_version(text)
            return uptime, mem_percentage , os_version

    folder_path = "../master/server_out_folder/"
    text_files = extract_text_files(folder_path)
    all_servers = []

    # Regular expression pattern to extract the server index from the filename
    pattern = r"server(\d{1,2})"

    # Iterate over each text file
    for file_path in text_files:
        server = {}

        # Extract the server index from the filename
        match = re.search(pattern, file_path, re.IGNORECASE)
        if match:
            server_index = int(match.group(1))
            server["index"] = server_index - 1

            # Extract values from the text file
            uptime, mem_percentage , os_version = extract_values_from_text(file_path)

            # Store the values in the server dictionary
            server["uptime"] = uptime
            server["memory"] = mem_percentage
            server["os"] = os_version

            all_servers.append(server)

    return all_servers


# #Test the function
# servers = generate_array()
# for server in servers:
#     print(f"Server{server['index']:02}: Uptime={server['uptime']}, Memory={server['memory']}")
