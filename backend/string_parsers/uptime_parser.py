def extract_uptime_value(input_string):
    if input_string.find("uptime -p_loc"):
        start_index = input_string.find(
            "up "
        )  # Find the start index of the uptime value
        length = len("up ")
        if start_index != -1:
            end_index = input_string.find(
                "\n", start_index
            )  # Find the end index of the uptime value
            if end_index != -1:
                uptime_value = input_string[
                    start_index + length : end_index
                ].strip()  # Extract the uptime value
                return uptime_value
    return None


# # Example usage
# str = '''
# uptime -p_loc: up 2 hours, 7 minutes
# '''

# uptime_value = extract_uptime_value(str)
# if uptime_value:
#     print("Uptime:", uptime_value)
# else:
#     print("Uptime value not found.")
