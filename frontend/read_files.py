import os


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
                all_file_contents.append(file_content)
                file_names.append(file_path[-12:])

    return all_file_contents, file_names
