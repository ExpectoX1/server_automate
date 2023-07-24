# Server Performance Monitoring v1.0

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

## Project Features and Technologies Used.

When the application starts up . All the servers are pinged by ansible and the frontend code runs, and the status of all the servers are displayed. The servers which are not active will be displayed as "Not Ready". All the servers which are active, ansible will run commands mentioned in the .ini file under the `[server0x-command]`. The result of running the command will be displayed on the screen (have to set it up) and if a command fails or doesn't run , ansible will throw an error. 
Every time the code runs , the log file gets appended `master/logs/error_logs` where you can see the execution status of the appliction. Also , all the ansible outputs are appended in a file under , `master/logs/ansible_backup`.

