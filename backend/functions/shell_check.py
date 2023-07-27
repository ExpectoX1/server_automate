import streamlit as st


def check_shell(command):
    arr = ["rm", "sudo"]
    for disallowed_command in arr:
        if disallowed_command in command:
            st.error("'" + command + "'" + " is not allowed, contact admin")
            return "invalid"
    return command


# print(check_shell("date"))
