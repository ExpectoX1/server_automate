import streamlit as st
from streamlit.components.v1 import html

import time

import sys

sys.path.append("../")
from backend.functions.config_parser import parse_servers

# from backend.StringParsers.output_file_parser import generate_array
sys.path.append("../backend/string_parsers/")

from backend.string_parsers.output_file_parser import generate_array
from backend.functions.ansible import ansible_backup, ansible_backend
from backend.functions.log import log_write
from backend.functions.file_checking import create_dead_files, master_ini_file


# Create Streamlit application
@st.cache_data
def Streamlit():
    # Call the parse_servers function with the config file path
    try:
        st.title("Server Performance Monitoring v1.0")
        st.write("Server Health Status: ")

        ini_file = master_ini_file()

        servers = parse_servers(ini_file)

        start_time = time.time()
        ansible_backend(servers)
        end_time = time.time()

        execution_time = end_time - start_time
        log_write("Execution time: " + str(int(execution_time)) + " seconds")
        
        create_dead_files(ini_file)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("./main.css")

        # Display server status

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
        for idx, server in enumerate(servers):
            status_color = "ready" if server["status"] == "Ready" else "not-ready"
            ready_not_ready = "green" if server["status"] == "Ready" else "red"
            data = generate_array()
            # expander_state = st.empty()
            # expander_opened = expander_state.button(f"Open Expander {idx}", key=f"expander_{idx}")

            st.write(
                f"""
                <div class="server-card">
                    <p>{server['host_name']}</p>
                    <p>{server['server_loc']}</p>
                    <p>{server['os_version']}</p>
                    <p style="color:{ready_not_ready}">{server['status']}</p>
                    <p>{data[idx]["uptime"]}</p>
                    <button id="button" class="status-indicator {status_color}" key=f"button_{idx}"></button>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.expander(f"'"):
                st.markdown(
                    f'<p class="expander-card">Memory Usage: {data[idx]["memory"]}</p>',
                    unsafe_allow_html=True,
                )
        # time.sleep(60)
        # st.experimental_rerun()
        ansible_backup()

    except Exception as e:
        log_write(str(e))
        st.warning(e, icon="⚠️")
        # time.sleep(60)
        # st.experimental_rerun()


if __name__ == "__main__":
    try:
        # while(True):
        Streamlit()

        # time.sleep(30)
        # inp =input("Type Exit to Exit")
        # if(inp.lower() == exit):
        #     break

    except Exception as e:
        log_write(str(e))
        st.warning(e, icon="⚠️")
