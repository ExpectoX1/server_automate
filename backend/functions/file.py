import glob
import datetime
import os
import re
# from config_parser

def create_dead_files(config_file):
    print("Going to print dead files")
    # server_names = ini_file(config_file)
    read_files = glob.glob("../master/server_out_folder/server*")
    

def ansible_backup():
    read_files = glob.glob("../master/server_out_folder/server*")
    backup_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    with open("../master/logs/ansible_backup/" + backup_name, "wb+") as outfile:
        for f in read_files:
            pattern = r'server\d+'
            match = re.search(pattern,f)
            with open(f, "rb") as infile:
                outfile.write(match.group().encode('utf-8') + "\n".encode('utf-8') + infile.read() + "\n".encode('utf-8'))
    for f in read_files:
        os.remove(f)
