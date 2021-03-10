/#### DevOps_online_Lviv_2020Q42021Q1

## TASK 8.1

### Continuous integration / Continuous delivery (deployment).

____

In this part of the training, I started working with ***Jenkins***. Jenkins is a stand-alone open automation server that can be used to automate a variety of tasks related to creating, testing, and delivering or deploying software.
Jenkins can be installed through its own system packages, Docker, or even run standalone on any machine with a Java runtime (JRE) installed. I installed it on a CentOs virtual machine. 

I repeated the examples from our lecture.

![image](./images/8.1_simple_joba.png)

![image](./images/8.1_jenkins_jobdeploy_1.png)

On another VM with Ubuntu I Installed ***Apache*** HTTP Server -- the world's most popular Web server software.

![image](./images/8.1_ub_vm2_apache.png)

![image](./images/8.1_jenkins_first_project.png)

![image](./images/8.1_jenkins_Publish_over_SSH.png)

![image](./images/8.1_jenkins_Publish_over_SSH_2.png)

After that I worked on ***Git*** and ***GitHub***

![image](./images/8.1_jenkins_Git.png)

![image](./images/8.1_jenkins_Git2.png)

![image](./images/8.1_jenkins_sheduler.png)

Then I configured the ***node*** (on VM Ubuntu) for Jenkins.

![image](./images/8.1_jenkins_node1.png)

I installed another copy of Apache in Docker on my Raspberry PI. And set up automation, when I push something to GitHub, it will be dragged using Node and published on the Raspberry.

![image](./images/HA/8.1_jenkins_HA_1.png)

![image](./images/HA/8.1_jenkins_node1.png)

![image](./images/HA/8.1_jenkins_HA_success.png)

![image](./images/HA/8.1_jenkins_HA_success_2.png)

![image](./images/HA/8.1_jenkins_HA_success_3.png)

____

#### Thanks!