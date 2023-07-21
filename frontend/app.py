import streamlit as st
import time
import sys

sys.path.append("../")
from backend.functions.config_parser import parse_servers

sys.path.append("../backend/string_parsers/")

from backend.string_parsers.output_file_parser import generate_array
from backend.functions.ansible import ansible_backup, ansible_backend
from backend.functions.log import log_write
from backend.functions.file_checking import create_dead_files, master_ini_file

refresh = True


def Streamlit():
    # Call the parse_servers function with the config file path
    try:
        st.title("Server Performance Monitoring v1.0")

        # Add a text input box to search for a specific server
        search_server_name = st.text_input("Search Server by Name:")

        st.write("Server Health Status: ")

        ini_file = master_ini_file()  # check for ini files in the master dir.
        servers, refresh_time = parse_servers(ini_file)  # parse the ini file.
        refresh_time = int(refresh_time)  # refresh time

        start_time = time.time()
        ansible_backend(servers)
        end_time = time.time()
        execution_time = end_time - start_time

        log_write("Execution time: " + str(int(execution_time)) + " seconds")

        create_dead_files(ini_file)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("./main.css")  # importing CSS

        # Filter servers based on the search_server_name if provided
        filtered_servers = servers
        if search_server_name:
            filtered_servers = [
                server
                for server in servers
                if server["host_name"].lower() == search_server_name.lower()
            ]

        # Display server status heading
        st.write(
            f"""
            <div class="server-card1 font-bold">
                <p class='font-bold'>Host Name</p>
                <p class='font-bold'>Location</p>
                <p class='font-bold'>OS Version</p>
                <p class='font-bold'>Ping Status</p>
                <p class='font-bold'>Uptime</p>
                <div class="status-indicator ready"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Display server status
        data_servers = generate_array()
        for server in filtered_servers:
            index = servers.index(server)
            status_color = "ready" if server["status"] == "Ready" else "not-ready"
            ready_not_ready = "green" if server["status"] == "Ready" else "red"
            st.write(
                f"""
                <div class="server-card">
                    <p>{server['host_name']}</p>
                    <p>{server['server_loc']}</p>
                    <p>{data_servers[index]['os']}</p>
                    <p style="color:{ready_not_ready}">{server['status']}</p>
                    <p>{data_servers[index]["uptime"]}</p>
                    <button id="button" class="status-indicator {status_color}" key=f"button_{server['host_name']}"></button>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.expander(f"'"):
                st.markdown(
                    f'<p class="expander-card">Memory Usage: {data_servers[index]["memory"]}</p>',
                    unsafe_allow_html=True,
                )

        if not search_server_name and not filtered_servers:
            st.write("No servers found.")
        elif search_server_name and not filtered_servers:
            st.write(f"No server with the name '{search_server_name}' found.")

        ansible_backup()
        min_mul = 1  ## change this to 60 for mins
        if refresh_time == None or refresh_time <= 0:
            log_write(
                "Invalid refresh variable value, reverting the refresh value to 10s"
            )
            refresh_time = 10
            min_mul = 1
        if refresh:
            time.sleep(refresh_time * min_mul)
            log_write("Re-running the script")
            print("Please Wait...Refreshing App")
            st.experimental_rerun()

    except Exception as e:
        log_write(str(e))
        st.warning(e, icon="⚠️")


if __name__ == "__main__":
    try:
        print(f"Application Running , open browser and go to http://localhost:8501")

        # Add an on_change event for the text box to refresh on Enter key press

        Streamlit()

    except Exception as e:
        log_write(str(e))
        st.warning(e, icon="⚠️")
