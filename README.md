# Server Performance Monitoring v1.1.0

## To run this application, follow these steps:

1. Clone the repository:<br>
   `git clone https://github.com/ExpectoX1/server_automate` <br>
   `cd server_automate`

2. Install the required dependencies: <br>
   `bash install_dependencies.sh` (contains , `sudo apt update`)

3. Check the master directory for the configuration file (examples.ini). Ensure it contains the necessary server information.

4. Navigate to the frontend dir<br>
   `cd frontend`

5. Run the Streamlit application:<br>
   `streamlit run app.py`

6. Open your web browser and go to http://localhost:8501 to access the application.

Alternatively you can run directly by running - `bash server_automate/run_app.sh` in the cli 

## Project Features and Technologies Used.

When the application starts up . All the servers are pinged by ansible and the frontend code runs, and the status of all the servers are displayed. The servers which are not active will be displayed as "Not Ready". All the servers which are active, ansible will run commands mentioned in the .ini file under the `[server0x-command]`. The result of running the command will be displayed on the screen (have to set it up) and if a command fails or doesn't run , ansible will throw an error.
Every time the code runs , the log file gets appended `master/logs/error_logs` where you can see the execution status of the appliction. Also , all the ansible outputs are appended in a file under , `master/logs/ansible_backup`. Any command mentioned in the .ini file under `[server0x-command]` will be executed by ansible on the respective server and it's output if not displayed on the frontend it will be printed out in a file under `master/logs/ansible_backup`. There is also a search bar in you can search for dedicated servers. In the side bar there are buttons provided to view the raw contents of a file as well as to open the inbuilt terminal and execute commands.

### Technologies Used

<ul>
<b>1. Streamlit <br> </b>
<b>2. Ansible </b>
</ul>

#### Streamlit:

Streamlit is a user-friendly and powerful Python library designed for creating web applications with ease. With Streamlit, developers can transform their data scripts into interactive web apps effortlessly, eliminating the need for complex web development frameworks. It allows users to visualize data, generate plots, and display machine learning models, all through simple Python code. The real strength of Streamlit lies in its simplicity; even those with minimal web development experience can quickly build impressive and interactive web applications. Whether it's data exploration, prototyping, or sharing insights, Streamlit empowers developers to turn their ideas into functional and attractive web applications without the hassle of traditional web development. Docs : https://docs.streamlit.io/.

#### Ansible:

Ansible is an open-source automation tool used for managing IT infrastructure and application deployment. It simplifies tasks through a human-readable language, requiring no additional software on managed nodes due to its agentless architecture. Ansible is versatile, efficient, and widely adopted for streamlining complex workflows and accelerating infrastructure and application deployment. Docs: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4

We have also used many parsers like , `.txt` , `.ini` and `.config` parsers. All of them were made form scratch.

#### App Demo:

![image](https://github.com/ExpectoX1/server_automate/assets/79239242/479d13c9-4090-4748-822d-f11368dd5696)
