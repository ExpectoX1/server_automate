import glob
from pathlib import Path
import sys
sys.path.append("../")
from backend.functions.config_parser import ini_parser

#creating empty files in cases ansible commands not being run
def create_dead_files(ini_file):
    print("Going to print dead files")
    server_names = ini_parser(ini_file)
    read_files = glob.glob("../master/server_out_folder/server*")
    print(read_files)
    for names in server_names.sections():
        if "-command" not in names and ("../master/server_out_folder/" + names + ".txt") not in read_files:
            print(names)
            with open('../master/server_out_folder/' + names + ".txt", 'w') as fp:
                pass

#Note: dont put spaces in the beginning of file path string or it will throw an error
def valid_path(file_path):
    my_file = Path(file_path)
    try:
        my_file.resolve(strict=True)
        return file_path
    except FileNotFoundError:
        raise Exception(file_path + " doesnt exist")