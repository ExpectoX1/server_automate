import datetime

import sys
sys.path.append("../../master/Logs/")

import datetime

def log_write(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {str(data)}"

    try:
        log_file_name = datetime.datetime.now().strftime("%Y-%m-%d") + "_log_file.txt"
        with open("../master/Logs/"+log_file_name, "a+") as log_file:
            log_file.write(log_entry + "\n")
           
    except Exception as e:
        error_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_entry = f"{error_timestamp}: Failed to write to log file - {str(e)}"
        print(error_entry)  # or log it in another file for error tracking


