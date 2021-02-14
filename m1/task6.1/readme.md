/#### DevOps_online_Lviv_2020Q42021Q1

## TASK 6.1

### Module 6 Networking with Linux.

____

1) Using VirtualBox I modeled connection according to scheme provided in task. I maked setups ethernets controllers in both operating systems.

In CentOs, in addition to the NAT interface (which automatically accepts the IP address), I set the IP address for the internal connection.

![image](./images/6.1-cent_ifconfig_ping.png)

Using netplan I set a static IP address In Ubuntu for the internal connection.

![image](./images/6.1-ub_netplan.png)

2) Next, I enable forwarding in Centos.

![image](./images/6.1-ip_forward.png)

After that, I installed and configured iptables and disabled the firewall.

![image](./images/6.1-iptables.png)

3) Than I checked the route from VM2 to Host.

![image](./images/6.1-mtr_host.png)

4) I checked the access to the Internet.

![image](./images/6.1-ping_google2.png)

5) I determined which resource has an IP address of 8.8.8.8.

![image](./images/6.1-nslookup.png)

6) I determined which IP address belongs to resource epam.com.

![image](./images/6.1-dig_epam.png)

7) I determined the default gateway for my HOST and display routing table.

![image](./images/6.1-route_host2.png)

8) I used the mtr command to track the route to google.com.
  
![image](./images/6.1-route_google.com.png)
____

#### Thanks!