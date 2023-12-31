import streamlit as st
import time
import sys


sys.path.append("../")
sys.path.append("../backend/string_parsers/")
import datetime
from streamlit_autorefresh import st_autorefresh
from backend.functions.read_files import read_files_in_folder
from backend.functions.config_parser import parse_servers
from backend.string_parsers.output_file_parser import generate_array
from backend.functions.ansible import ansible_backup, ansible_backend, delete_ansible
from backend.functions.log import log_write
from backend.functions.file_checking import create_dead_files, master_ini_file
from backend.functions.shell import ansible_shell
from backend.functions.shell_check import check_shell


def refreshing():
    try:
        refresh = True
        mul = 1  # make this 60 later
        ini_file = master_ini_file()
        refesh_timer = parse_servers(ini_file)
        refesh_timer = int(refesh_timer[1])
        if refesh_timer < 0:
            log_write("Invalid refresh timer, returning to defaults")
            refesh_timer = 10
        refresh_count = st_autorefresh(refesh_timer * mul * 1000)  # in milli seconds
        print("Please Wait, refresh in progress...")
        log_write("Page Refreshing " + str(refresh_count + 1))
    except Exception as e:
        raise Exception(e)


def Streamlit():
    st.title("Server Performance Monitoring v1.1.0")
    # Call the parse_servers function with the config file path
    try:
        tabA , tabB = st.tabs(["App" , "How to Run"])
        
        delete_ansible()  # delete files in the server_out_folder
        
        with tabA:
            # Add a text input box to search for a specific server
            search_server_name = st.text_input("Search Server by Hostname:")
            ini_file = master_ini_file()  # check for ini files in the master dir.
            servers, refresh_time = parse_servers(ini_file)  # parse the ini file.

            # Getting Execution Time
            start_time = time.time()
            ansible_backend(servers)
            end_time = time.time()
            execution_time = end_time - start_time
            log_write("Execution time: " + str(int(execution_time)) + " seconds")

            # Create Missing Files
            create_dead_files(ini_file)

            # Load CSS
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
            if filtered_servers != servers:
                log_write("Searched For a Server")
                log_write(filtered_servers)
            if not filtered_servers:  # Check if there are no matching servers
                st.write("No servers Found.")
                log_write("No servers Found")
                return  # Exit the function to avoid the refresh logic

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
        with tabB:
            def read_readme_file(file_path):
                with open(file_path, "r") as file:
                    content = file.read()
                return content  
            readme = read_readme_file("../README.md")
            st.code(readme , language="text")

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        st.toast("Success: Latest Info Displaying " + "Time: " + timestamp)
        st.toast("Backend Execution Time : " + str(int(execution_time)) + " seconds")
        ansible_backup()

        st.sidebar.title("Custom Outputs")
        folderpath = "../master/server_out_folder"
        (contents, txtname) = read_files_in_folder(folderpath)
        tab1, tab2, tab3 = st.sidebar.tabs(["Custom Outputs", "Terminal", "Overview"])
        with tab1:
            for i in range(0, len(contents)):
                # if st.button("View Contents of : " + servers[i]["host_name"]):
                if contents[i] == "":
                    st.code(servers[i]["host_name"] + " Not Reachable check logs")
                    st.toast(servers[i]["host_name"] + " Not Reachable check logs")
                    st.download_button(
                        label="Download " + txtname[i],
                        data=servers[i]["host_name"] + " Not Reachable",
                        file_name=txtname[i],
                    )
                else:
                    st.code(contents[i])
                    st.download_button(
                        label="Download " + txtname[i],
                        data=contents[i],
                        file_name=txtname[i],
                    )
                st.divider()
        with tab2:
            shell = st.text_area(
                "Enter the command you want to Execute (Press Ctrl+Enter)",
                height=100,
            )
            if shell != "":
                shell = check_shell(shell)
                if shell != "invalid":
                    ansible_shell(shell)
                    contents, filename = read_files_in_folder(
                        "../master/shell_out_folder"
                    )
                    for i in range(0, len(filename)):
                        st.divider()
                        temp = servers[i]["host_name"]
                        st.write(
                            f"<p class='custom-paragraph'>{temp}</p>",
                            unsafe_allow_html=True,
                        )
                        st.code(contents[i], language="vim", line_numbers=True)

        with tab3:
            for server in servers:
                if server["status"] == "Ready":
                    st.code(server["host_name"] + " -- " + server["status"] + " 🟢")
                else:
                    st.code(server["host_name"] + " -- " + server["status"] + " 🔴")

            # call command here

    except Exception as e:
        log_write(str(e))
        st.toast(e, icon="⚠️")


if __name__ == "__main__":
    try:
        start_t = time.time()
        print(f"Application Running , open browser and go to http://localhost:8501")
        refreshing()
        Streamlit()
        end_t = time.time()
        st.toast("Total Execution Time: " + str(int(end_t - start_t)) + " seconds")

    except Exception as e:
        log_write(str(e))
        st.toast(e, icon="⚠️")
