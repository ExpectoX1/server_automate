#!bin/bash
# Install system-level dependencies using apt-get
sudo apt-get update
sudo apt-get install -y sshpass 
#note: to use ansible with password you must once ssh into server and add fingerprint
#note2: If your private key has a passphrase use ssh agent to use the passphrase automatically

# Install Python packages using pip
pip install -r requirements.txt
