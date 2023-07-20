def extract_os_version(input_string):
    if input_string.find("os_version_loc"):
        start_index = input_string.find(
            "os_version_loc:"
        )  # Find the start index of the uptime value
        length = len("os_version_loc:")
        if start_index != -1:
            end_index = input_string.find(
                "\n", start_index
            )  # Find the end index of the uptime value
            if end_index != -1:
                os_version = input_string[
                    start_index + length : end_index
                ].strip()  # Extract the uptime value
                return os_version
    return None


##Test function
# print(extract_os_version(str))
