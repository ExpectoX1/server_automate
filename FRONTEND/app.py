import streamlit as st
from streamlit.components.v1 import html

import time

import sys

sys.path.append('../')
from MASTER.config_parser import parse_servers
from MASTER.log import log_write
# from backend.StringParsers.output_file_parser import generate_array
sys.path.append("../backend/StringParsers/")

from backend.StringParsers.output_file_parser import generate_array
from backend.functions.ansible import ansible_ping, ansible_playbook
from backend.functions.parse import add_host






# Create Streamlit application
@st.cache_data
def Streamlit():
    # Call the parse_servers function with the config file path
    try:
        html('''
                        <script></script>
                        ''' , height=0 ,width=0)
        
        st.title("Server Performance Monitoring v1.0")
        st.write("Server Health Status: ")

        servers = parse_servers("../MASTER/examples.ini")

        #Take out the pingless servers and insert that data to add_host
        def backend_func():
            print("Start of backend")
            add_host()

            print("adding host..")
            log_write("adding host success")

            ansible_ping()

            print("Pinging Servers")
            log_write("Ping Success")
            print("Running SSH Commands")

            ansible_playbook()

            print("Writing Files")
            log_write("Writing Files")
            log_write("Backend Success")
            print("Backend Success")
        
        start_time = time.time()
        backend_func()
        end_time = time.time()

        execution_time = end_time - start_time
        log_write("Execution time: " + str(execution_time) + " seconds")
        print("Execution time:", execution_time, "seconds")

        
    
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
            unsafe_allow_html=True
        )

        # Display server status
        for idx, server in enumerate(servers):
            status_color = "ready" if server["status"] == "Ready" else "not-ready"
            ready_not_ready = "green" if server["status"] == "Ready" else "red"
            

            expander_state = st.empty()
            # expander_opened = expander_state.button(f"Open Expander {idx}", key=f"expander_{idx}")
            st.write(
                f"""
                <div class="server-card">
                    <p>{server['host_name']}</p>
                    <p>{server['server_loc']}</p>
                    <p>{server['os_version']}</p>
                    <p style="color:{ready_not_ready}">{server['status']}</p>
                    <p>{server['server_uptime']}</p>
                    <button id="button" class="status-indicator {status_color}" key=f"button_{idx}"></button>
                </div>
                """,
                unsafe_allow_html=True
            )
            with st.expander(f"'"):
                # data = generate_array()
                # print(data[0])
                # sys.path.append("/backend/String_parsers/")
                data = generate_array()
                st.write("Uptime - "+data[idx]["uptime"])
                st.write("Memory Usage - "+data[idx]["memory"])
    
                    
    except Exception as e:
        log_write(str(e))
        st.warning(e, icon="⚠️")


if __name__ == "__main__":
    try:
        
        Streamlit()
    except Exception as e:
        log_write(str(e))
        st.warning(e,icon="⚠️")

