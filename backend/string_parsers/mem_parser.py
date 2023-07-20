import re


def extract_percentage_value(input_string):
    percentage_pattern = (
        r"\b(\d+%)\s\/\s"  # Regular expression pattern to match a percentage value
    )
    match = re.search(percentage_pattern, input_string)
    if match:
        percentage_value = match.group(1)
        return percentage_value
    return None


# # Example usage
# str= '''
# df -H_loc: Filesystem                         Size  Used Avail Use% Mounted on
# tmpfs                              206M  1.4M  205M   1% /run
# /dev/mapper/ubuntu--vg-ubuntu--lv   18G  8.0G  8.4G  49% /
# tmpfs                              1.1G     0  1.1G   0% /dev/shm
# tmpfs                              5.3M     0  5.3M   0% /run/lock
# /dev/sda2                          2.1G  265M  1.7G  14% /boot
# tmpfs                              206M  4.1k  206M   1% /run/user/1000
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/23290f2a6e4c2682bb8dd395e5fe4b5b414cfc9417a75565e48546ef2f130846/shm
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/6a4041091afaa8527a45004037df27ce91b59d702f0d62a1176bf4469a36cde8/shm
# shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/0ff38d990a4f5ae9fe2ad87965c64cad95d7f6e40531161a338dcbf9f437f3f1/shm
# top -n 1_loc: [?1h=[?25l[H[2J(B[mtop - 07:49:29 up  2:43,  2 users,  load average: 2.39, 2.81, 5.49(B[m[39;49m(B[m[39;49m[K
# Tasks:(B[m[39;49m[1m 138 (B[m[39;49mtotal,(B[m[39;49m[1m   1 (B[m[39;49mrunning,(B[m[39;49m[1m 137 (B[m[39;49msleeping,(B[m[39;49m[1m   0 (B[m[39;49mstopped,(B[m[39;49m[1m   0 (B[m[39;49mzombie(B[m[39;49m(B[m[39;49m[K
# %Cpu(s):(B[m[39;49m[1m  0.0 (B[m[39;49mus,(B[m[39;49m[1m  0.0 (B[m[39;49msy,(B[m[39;49m[1m  0.0 (B[m[39;49mni,(B[m[39;49m[1m 92.3 (B[m[39;49mid,(B[m[39;49m[1m  0.0 (B[m[39;49mwa,(B[m[39;49m[1m  0.0 (B[m[39;49mhi,(B[m[39;49m[1m  7.7 (B[m[39;49msi,(B[m[39;49m[1m  0.0 (B[m[39;49mst(B[m[39;49m(B[m[39;49m[K
# MiB Mem :(B[m[39;49m[1m   1964.0 (B[m[39;49mtotal,(B[m[39;49m[1m     69.6 (B[m[39;49mfree,(B[m[39;49m[1m    877.7 (B[m[39;49mused,(B[m[39;49m[1m   1016.7 (B[m[39;49mbuff/cache(B[m[39;49m(B[m[39;49m[K
# MiB Swap:(B[m[39;49m[1m   2048.0 (B[m[39;49mtotal,(B[m[39;49m[1m   2041.7 (B[m[39;49mfree,(B[m[39;49m[1m      6.3 (B[m[39;49mused.(B[m[39;49m[1m    931.2 (B[m[39;49mavail Mem (B[m[39;49m(B[m[39;49m[K
# [K
# [7m    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  (B[m[39;49m[K
# (B[m 163636 root      20   0 1122460 397628  94896 S  12.5  19.8   0:40.38 kubelite (B[m[39;49m[K
# (B[m   5853 root      20   0 1394196  58772  43780 S   6.2   2.9   2:37.29 calico-+ (B[m[39;49m[K
# (B[m[1m 181195 rithvik   20   0   10780   4212   3516 R   6.2   0.2   0:00.02 top      (B[m[39;49m[K
# (B[m      1 root      20   0  166628  11224   8076 S   0.0   0.6   0:43.50 systemd  (B[m[39;49m[K
# (B[m      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd (B[m[39;49m[K
# (B[m      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp   (B[m[39;49m[K
# (B[m      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par+ (B[m[39;49m[K
# (B[m      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 slub_fl+ (B[m[39;49m[K
# (B[m      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns    (B[m[39;49m[K
# (B[m      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+ (B[m[39;49m[K
# (B[m     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_perc+ (B[m[39;49m[K
# (B[m     11 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_tas+ (B[m[39;49m[K
# (B[m     12 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_tas+ (B[m[39;49m[K
# (B[m     13 root      20   0       0      0      0 S   0.0   0.0   0:14.03 ksoftir+ (B[m[39;49m[K
# (B[m     14 root      20   0       0      0      0 I   0.0   0.0   0:04.68 rcu_sch+ (B[m[39;49m[K
# (B[m     15 root      rt   0       0      0      0 S   0.0   0.0   0:00.11 migrati+ (B[m[39;49m[K
# (B[m     16 root     -51   0       0      0      0 S   0.0   0.0   0:00.00 idle_in+ (B[m[39;49m[K[?1l>[25;1H
# [?12l[?25h[K
# uptime -p_loc: up 2 hours, 43 minutes

# '''

# percentage_value = extract_percentage_value(str)
# if percentage_value:
#     print("Percentage:", percentage_value)
# else:
#     print("Percentage value not found.")
