import datetime
import sys
from backend.functions.file_checking import valid_path

sys.path.append("../../master/logs/")

def log_write(data):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: {str(data)}"
        log_file_name = datetime.datetime.now().strftime("%Y-%m-%d") + "_log_file.txt"
        with open(valid_path("../master/logs/error_logs/") + log_file_name, "a+") as log_file:
            log_file.write(log_entry + "\n")
           
    except Exception as e:
        error_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_entry = f"{error_timestamp}: Failed to write to log file - {str(e)}"
        print(error_entry)  # or log it in another file for error tracking


