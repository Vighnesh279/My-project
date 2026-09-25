# EXP-04 - Ansible Configuration Management



## Aim



To understand and implement configuration management and automation using Ansible for provisioning and configuring a web server.



## Tools Used



- Ansible

- Ubuntu Linux

- SSH

- Nginx

- Command Line



## Ansible Inventory



The managed web server was defined in the Ansible inventory file:



inventory.ini



The inventory contains the web server under the `web` group.



## Playbook



The Ansible playbook is:



site.yml



The playbook performs the following tasks:



1. Installs Nginx.

2. Ensures that the Nginx service is running and enabled.

3. Deploys the required HTML page to the Nginx web directory.



## Connectivity Test



Ansible connectivity to the managed host was verified using the Ansible ping module.



A successful response returned:



ping: pong



## Playbook Execution



The playbook was executed using:



ansible-playbook -i inventory.ini site.yml



The required tasks were successfully executed on the managed web server.



## Verification



The deployed Nginx web page was accessed and verified successfully.



The experiment also demonstrated Ansible idempotence by running the playbook again and observing that no unnecessary changes were made.



## Files



The experiment files included:



- inventory.ini

- site.yml



## Evidence



The complete faculty submission is available here:



Submission/DEV_VIG4.pdf



## Result



Ansible was successfully used to automate web server configuration. Nginx was installed and configured, the service was enabled and started, and the required web page was deployed and verified.


