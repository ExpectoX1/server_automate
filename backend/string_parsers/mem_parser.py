import re


def extract_percentage_value(input_string):
    percentage_pattern = (
        r"\b(\d+%)\s\/\s"  # Regular expression pattern to match a percentage value
    )
    match = re.search(percentage_pattern, input_string)
    if match:
        percentage_value = match.group(1)
        return percentage_value
    return None
