import functions.parse as parse
import functions.ansible as ansible

output1 = parse.add_host()
output2 = ansible.ansible_playbook()
print(output1)
print(output2)