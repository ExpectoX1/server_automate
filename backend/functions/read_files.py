import os
import time


def extract_info(input_string):
    lines = input_string.strip().split("\n")
    result = []
    length = 0
    count = 0
    for i, line in enumerate(lines):  # Use enumerate to get index 'i'
        if "_loc:" in line:
            command = line.split("_loc:")[0].strip()
            info = line.split("_loc:")[-1].strip()
            length = 0
            result.append(command + " (command " + str(i - count + 1) + ") ::: " + info)
            length = len(command + " (command" + str(i - count + 1) + ") ::: ")
        else:
            result.append(" " * length + line)
            length = 0
            count = count + 1
    return "\n".join(result)


def read_files_in_folder(folder_path):
    all_file_contents = []
    file_names = []

    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        raise ValueError("Folder path does not exist.")

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Loop through each file and read its content
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(
            file_path
        ):  # Ensure we are dealing with files, not subdirectories
            with open(file_path, "r") as f:
                file_content = f.read()
                all_file_contents.append(extract_info(file_content))
                file_names.append(file_path[-12:])
    sorted_contents = sorted(zip(file_names, all_file_contents), reverse=False)
    sorted_file_names, sorted_all_file_contents = zip(*sorted_contents)
    return sorted_all_file_contents, sorted_file_names