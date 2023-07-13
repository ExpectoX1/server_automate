import re

def extract_percentage_value(input_string):
    if (input_string.find("df -H_loc")):
        percentage_pattern = r'\b(\d+%)\s\/\s'  # Regular expression pattern to match a percentage value
        match = re.search(percentage_pattern, input_string)
        if match:
            percentage_value = match.group(1)
            return percentage_value
        return None
    return None

# # Example usage
# str= '''
# df -H_loc: Filesystem                         Size  Used Avail Use% Mounted on
# tmpfs                              206M  1.4M  205M   1% /run
# /dev/mapper/ubuntu--vg-ubuntu--lv   18G  8.0G  8.5G  49% /
# tmpfs                              1.1G     0  1.1G   0% /dev/shm
# tmpfs                              5.3M     0  5.3M   0% /run/lock
# /dev/sda2                          2.1G  265M  1.7G  14% /boot
# tmpfs                              206M  4.1k  206M   1% /run/user/1000
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/23290f2a6e4c2682bb8dd395e5fe4b5b414cfc9417a75565e48546ef2f130846/shm
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/6a4041091afaa8527a45004037df27ce91b59d702f0d62a1176bf4469a36cde8/shm
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/0ff38d990a4f5ae9fe2ad87965c64cad95d7f6e40531161a338dcbf9f437f3f1/shm 
# uptime -p_loc: up 33 minutes 

# '''

# percentage_value = extract_percentage_value(str)
# if percentage_value:
#     print("Percentage:", percentage_value)
# else:
#     print("Percentage value not found.")
