import functions.parse as parse
import functions.ansible as ansible


parse.add_host()
ansible.ansible_ping()
# output2 = ansible.ansible_playbook()
# ansible.ansible_ping()
# print(output2)