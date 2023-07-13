from check_parsers.uptime_parser import extract_uptime_value
from check_parsers.mem_parser import extract_percentage_value
import os
import sys

# Write code for importing all the data from all the servers and storing in an array

def genetate_array():
    def extract_text_files(folder_path):
        text_contents = []

        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a text file
            if os.path.isfile(file_path) and file_name.lower().endswith('.txt'):
                # Read the contents of the text file
                with open(file_path, 'r') as file:
                    text_contents.append(file.read())

        return text_contents

    def extract_values_from_text(text):
        uptime = extract_uptime_value(text)
        mem_percentage = extract_percentage_value(text)
        print(mem_percentage)
        return uptime, mem_percentage

    folder_path = "../../MASTER/server_folder"
    text_files = extract_text_files(folder_path)
    all_arrays = []

    # Iterate over each text file
    for text in text_files:
        uptime_array = []
        mem_array = []

        # Extract values from the text file
        uptime, mem_percentage = extract_values_from_text(text)

        # Store the values in arrays
        uptime_array.append(uptime)
        mem_array.append(mem_percentage)

        all_arrays.append((uptime_array, mem_array))

    return all_arrays

# Test the function
arrays = genetate_array()
for i, (uptime_array, mem_array) in enumerate(arrays):
    print(f"Server {i+1} - Uptime: {uptime_array}, Memory: {mem_array}")
