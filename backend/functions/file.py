import glob
import datetime
import os
import re

def ansible_backup():
    read_files = glob.glob("../master/server_out_folder/server*")
    backup_name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".txt"
    with open("../master/Logs/ansible_backup" + backup_name, "wb") as outfile:
        for f in read_files:
            pattern = r'server\d+'
            match = re.search(pattern,f)
            with open(f, "rb") as infile:
                outfile.write(match.group().encode('utf-8') + "\n".encode('utf-8') + infile.read() + "\n".encode('utf-8'))
    for f in read_files:
        os.remove(f)

def create_dead_files():
    print("Going to print dead files")