# Ansible
## How to run
1. Get your Openstack Password
    - <img src="docs/1.jpg" width=50%/>
    - <img src="docs/2.jpg" width=50%/>

2. Deploy instances on the Nectar
    - |role|description|
      |---|---|
      |common|Install Python-pip, openstacksdk and update pip on hosts|
      |show-images|Show all available Openstack images|
      |create-volumes|Create volumes from vars|
      |create-security-groups|Create security groups and their rules|
      |create-instances|Create instances on NeCTAR<br/>Add hosts to Ansible in-memory inventory
    - ```./deploy_instances_debug.sh```  
    - ```./deploy_instances.sh```

3. Configure instances environments on the Nectar
    - |role|description|
      |---|---|
      |add-proxy|Add proxy in /etc/environment<br/>Reboot the instance|
    - If using windows, 
        1. ```cp ./NectarGroupKey.pem ~/.ssh/```
        2. ```chmod 400 ~/.ssh/NectarGroupKey.pem```
    - ```./configure_instances_debug.sh```

4. Deploy Applications on the Nectar instances
    - ``` ```

5. Remove instances on the Nectar
    - ```./remove_deploy_instances.sh```

## Notes
1. initialize a role
    - ```cd roles```
    - ```ansible-galaxy init test-role-1```
