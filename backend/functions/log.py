import datetime
import sys
import os
import zipfile
from backend.functions.file_checking import valid_path

sys.path.append("../../master/logs/")


def log_write(data):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: {str(data)}"

        log_directory = valid_path("../master/logs/error_logs/")
        log_file_name = datetime.datetime.now().strftime("%Y-%m-%d") + "_log_file.txt"
        log_path = log_directory + log_file_name

        with open(
            log_path, "a+"
        ) as log_file:
            log_file.write(log_entry + "\n")

        #Zipping files when they get too large
        if os.path.getsize(log_path) > 100000:
            #Renaming log to full time stamp
            new_path = log_directory + timestamp + "_log_file.txt"
            os.rename(log_path, new_path)
            #Naming zip file as old log name
            zip_path = valid_path("../master/logs/error_backup/") +  datetime.datetime.now().strftime("%Y-%m-%d") + ".zip"
            with zipfile.ZipFile(zip_path, 'a+') as zip:
                zip.write(new_path)
            os.remove(new_path)

    except Exception as e:
        error_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_entry = f"{error_timestamp}: Failed to write to log file - {str(e)}"
        print(error_entry)  # or log it in another file for error tracking
