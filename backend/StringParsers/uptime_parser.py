def extract_uptime_value(input_string):

    index = input_string.find("uptime_loc")




    if index != -1:

        start_index = index + len("uptime_loc: ")

        end_index = input_string.find(" up", start_index)




        if end_index != -1:

            uptime_value = input_string[start_index:end_index].strip()

            return uptime_value

        else:

            return None

    else:

        return None




# Example usage

str = '''date_loc: Wed Jul 12 08:02:36 AM UTC 2023
df -H_loc: Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              206M  1.4M  205M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   18G  7.9G  8.5G  49% /
tmpfs                              1.1G     0  1.1G   0% /dev/shm
tmpfs                              5.3M     0  5.3M   0% /run/lock
/dev/sda2                          2.1G  265M  1.7G  14% /boot
tmpfs                              206M  4.1k  206M   1% /run/user/1000
shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/bc1f1f00592b771b072d5426e1e2a5a5aa22cef8e0829e7669eb8324c49a13d9/shm
shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/8c9032c0916e954c04efd7bc1a75d3a55ee7aef521f84071713ef023ce8ff5fa/shm
shm                                 68M     0   68M   0% /var/snap/microk8s/common/run/containerd/io.containerd.grpc.v1.cri/sandboxes/a3744834e19781cfa1247826c28f9fd97331a790bbac90e3a0ff662bbfaabcb9/shm
top -n 1_loc: [?1h=[?25l[H[2J(B[mtop - 05:50:43 up  1:44,  2 users,  load average: 4.92, 3.55, 2.54(B[m[39;49m(B[m[39;49m[K
Tasks:(B[m[39;49m[1m 140 (B[m[39;49mtotal,(B[m[39;49m[1m   7 (B[m[39;49mrunning,(B[m[39;49m[1m 133 (B[m[39;49msleeping,(B[m[39;49m[1m   0 (B[m[39;49mstopped,(B[m[39;49m[1m   0 (B[m[39;49mzombie(B[m[39;49m(B[m[39;49m[K
%Cpu(s):(B[m[39;49m[1m 54.5 (B[m[39;49mus,(B[m[39;49m[1m 27.3 (B[m[39;49msy,(B[m[39;49m[1m  0.0 (B[m[39;49mni,(B[m[39;49m[1m  0.0 (B[m[39;49mid,(B[m[39;49m[1m  0.0 (B[m[39;49mwa,(B[m[39;49m[1m  0.0 (B[m[39;49mhi,(B[m[39;49m[1m 18.2 (B[m[39;49msi,(B[m[39;49m[1m  0.0 (B[m[39;49mst(B[m[39;49m(B[m[39;49m[K
MiB Mem :(B[m[39;49m[1m   1964.0 (B[m[39;49mtotal,(B[m[39;49m[1m     69.2 (B[m[39;49mfree,(B[m[39;49m[1m    844.8 (B[m[39;49mused,(B[m[39;49m[1m   1050.0 (B[m[39;49mbuff/cache(B[m[39;49m(B[m[39;49m[K
MiB Swap:(B[m[39;49m[1m   2048.0 (B[m[39;49mtotal,(B[m[39;49m[1m   2042.5 (B[m[39;49mfree,(B[m[39;49m[1m      5.5 (B[m[39;49mused.(B[m[39;49m[1m    964.7 (B[m[39;49mavail Mem (B[m[39;49m(B[m[39;49m[K
[K
[7m    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  (B[m[39;49m[K
(B[m    834 root      20   0 1493080 225188  16952 S  43.8  11.2  11:00.00 k8s-dql+ (B[m[39;49m[K
(B[m[1m 146814 root      20   0 1006456  23244  20716 R  18.8   1.2   0:00.07 calico-+ (B[m[39;49m[K
(B[m 146823 root      20   0 1161100   9240   7640 S  12.5   0.5   0:00.02 runc     (B[m[39;49m[K
(B[m[1m 146830 rithvik   20   0   10776   4220   3508 R  12.5   0.2   0:00.02 top      (B[m[39;49m[K
(B[m    794 root      20   0  392596  12576  10372 S   6.2   0.6   0:11.28 udisksd  (B[m[39;49m[K
(B[m   3385 rithvik   20   0   17304  10020   8096 S   6.2   0.5   0:19.77 systemd  (B[m[39;49m[K
(B[m   5488 root      20   0 1393940  57516  43148 S   6.2   2.9   1:54.47 calico-+ (B[m[39;49m[K
(B[m      1 root      20   0  166760  12160   8428 S   0.0   0.6   0:31.58 systemd  (B[m[39;49m[K
(B[m      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd (B[m[39;49m[K
(B[m      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp   (B[m[39;49m[K
(B[m      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par+ (B[m[39;49m[K
(B[m      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 slub_fl+ (B[m[39;49m[K
(B[m      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns    (B[m[39;49m[K
(B[m      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+ (B[m[39;49m[K
(B[m     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_perc+ (B[m[39;49m[K
(B[m     11 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_tas+ (B[m[39;49m[K
(B[m     12 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_tas+ (B[m[39;49m[K[?1l>[25;1H
[?12l[?25h[K
uptime_loc:  08:02:35 up  3:56,  2 users,  load average: 2.50, 1.88, 1.90'''




uptime_value = extract_uptime_value(str)

if uptime_value:

    print("Uptime:", uptime_value)

else:

    print("Uptime value not found.")