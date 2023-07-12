import configparser
import platform
from subprocess import call
import streamlit as st
from streamlit.components.v1 import html
# Ping the host and return the status
def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return call(command) == 0

# Parse the server configurations from the config file
def parse_servers(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    servers = []
    for section in config.sections():
        server = {
            "host_name": config[section].get("host_name"),
            "server_loc": config[section].get("location"),
            "os_version": config[section].get("os_version"),
            "server_uptime": config[section].get("server_uptime"),
            "server_ip": config[section].get("server_ip"),
            "cummi_status": config[section].get("cummi_status")
        }
        server_address = server["server_ip"]
        if ping(server_address):
            server["status"] = "Ready"
        else:
            server["status"] = "Not Ready"
            #Functions to not ping()

        servers.append(server)
    return servers

# Create Streamlit application
def main():
    # Call the parse_servers function with the config file path
    servers = parse_servers("examples.ini")
    html('''
                    <script></script>
                    ''' , height=0 ,width=0)

    st.title("Server Performance Monitoring v1.0")
    st.write("Server Health Status: ")

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
        with st.expander(f"opn"):
            st.write(f"hi")
            


if __name__ == "__main__":
    main()
