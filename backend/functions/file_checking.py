import glob
from pathlib import Path
import sys

sys.path.append("../")
from backend.functions.config_parser import ini_parser


# creating empty files in cases ansible commands not being run
def create_dead_files(ini_file):
    try:
        server_names = ini_parser(ini_file)
        # List of all output files
        read_files = glob.glob("../master/server_out_folder/server*")
        for names in server_names.sections():
            if "DEFAULT_VAL" in names:
                continue
            if (
                "-command" not in names
                and (valid_path("../master/server_out_folder/") + names + ".txt")
                not in read_files
            ):
                # creates empty file if not found
                with open(
                    valid_path("../master/server_out_folder/") + names + ".txt", "w"
                ) as fp:
                    pass
    except Exception as e:
        raise Exception(e)


#Looking for the ini file path in master to be passed into config_parser.ini_file()
def master_ini_file():
    read_files = glob.glob("../master/*.ini")
    if len(read_files) != 1:
        raise Exception("Keep a single ini file in the master folder")
    else:
        return valid_path(read_files[0])


# Note: dont put spaces in the beginning of file path string or it will throw an error
#Checking if file/directory exists or not
def valid_path(file_path):
    try:
        my_file = Path(file_path)
        my_file.resolve(strict=True)
        return file_path
    except FileNotFoundError:
        raise Exception(file_path + " doesnt exist")
