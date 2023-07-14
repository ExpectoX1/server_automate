import sys
sys.path.append("../string_parsers/")
from uptime_parser import extract_uptime_value
from mem_parser import extract_percentage_value
import os

def generate_array():
    def extract_text_files(folder_path):
        text_files = []

        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a text file
            if os.path.isfile(file_path) and file_name.lower().endswith('.txt'):
                text_files.append(file_path)

        return text_files

    def extract_values_from_text(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            uptime = extract_uptime_value(text)
            mem_percentage = extract_percentage_value(text)
            return uptime, mem_percentage

    folder_path = "../master/server_out_folder"
    text_files = extract_text_files(folder_path)
    all_servers = []

    # Iterate over each text file
    for file_path in text_files:
        server = {}

        # Extract values from the text file
        uptime, mem_percentage = extract_values_from_text(file_path)

        # Store the values in the server dictionary
        server['uptime'] = uptime
        server['memory'] = mem_percentage

        all_servers.append(server)

    return all_servers

# Test the function
# servers = generate_array()
# for i, server in enumerate(servers):
#     print(f"Server0{i+1}: Uptime={server['uptime']}, Memory={server['memory']}")