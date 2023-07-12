def extract_uptime_value(input_string):

    index = input_string.find("uptime_loc")




    if index != -1:

        start_index = index + len("uptime_loc: ")

        end_index = input_string.find(" up", start_index)




        if end_index != -1:

            uptime_value = input_string[start_index:end_index].strip()

            return uptime_value

        else:

            return None

    else:

        return None




# Example usage

str = '''date: Wed Jul 12 05:13:40 AM UTC 2023

uptime_loc:  05:13:30 up  1:07,  2 users,  load average: 1.61, 0.92, 0.94'''




uptime_value = extract_uptime_value(str)

if uptime_value:

    print("Uptime:", uptime_value)

else:

    print("Uptime value not found.")