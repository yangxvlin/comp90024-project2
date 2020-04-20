# Ansible
## How to run
1. Get your Openstack Password
    - <img src="docs/1.jpg" width=50%/>
    - <img src="docs/2.jpg" width=50%/>

2. Deploy instances on the Nectar
    - <table>
        <tr>
            <th>Hosts</th>
            <th>role</th>
            <th>description</th>
        </tr>
        <tr>
            <td rowspan="5">localhost</td>
            <td>common</td>
            <td>Install Python-pip, openstacksdk and update pip on hosts</td>
        </tr>
        <tr>
            <td>show-images</td>
            <td>Show all available Openstack images</td>
        </tr>
        <tr>
            <td>create-volumes</td>
            <td>Create volumes from vars</td>
        </tr>
        <tr>
            <td>create-security-groups</td>
            <td>Create security groups and their rules</td>
        </tr>
        <tr>
            <td>create-instances</td>
            <td>Create instances on NeCTAR<br>Add hosts to Ansible in-memory inventory</td>
        </tr>
        </table>
    - ```./deploy_instances_debug.sh```  
    - ```./deploy_instances.sh```

3. Configure instances environments on the Nectar
    - <table>
        <tr>
            <th>Hosts</th>
            <th>role</th>
            <th>description</th>
        </tr>
        <tr>
            <td><span style="font-weight:normal">localhost</span></td>
            <td><span style="font-weight:normal">add-NectarGroupKey</span><br></td>
            <td><span style="font-weight:normal">copy /config/NectarGroupKey to ~/.ssh/</span><span style="font-weight:400;font-style:normal">NectarGroupKey</span><br></td>
        </tr>
        <tr>
            <td rowspan="4">instances</td>
            <td>add-proxy</td>
            <td>Add proxy in /etc/environment&lt;br/&gt;Reboot the instance</td>
        </tr>
        <tr>
            <td>install-dependencies</td>
            <td>sudo apt-get update; sudo apt-get install ['git', 'python3-dev', 'python3-pip', 'python3-setuptools', 'vim', 'python3-pip', 'libblacs-mpi-dev']<br>pip3 install ['wheel', 'mpi4py']</td>
        </tr>
        <tr>
            <td>setup-docker</td>
            <td>Install docker as well as setting up http proxy for docker</td>
        </tr>
        <tr>
            <td><span style="font-weight:normal">git-clone-source-repository</span><br></td>
            <td>configure git ssh key<br>clone the source code repository to the instances</td>
        </tr>
        </table>
    - No matter what OS you are, you should create a file: ```/config/GitHubKey.pem``` with **your GitHub private key**
    - ```./configure_instances_debug.sh```

4. Deploy Applications on the Nectar instances
    - ``` ```

5. Remove instances on the Nectar
    - ```./remove_deploy_instances.sh```

## Notes
1. initialize a role
    - ```cd roles```
    - ```ansible-galaxy init test-role-1```
2. use https://www.tablesgenerator.com/html_tables to modify the tables above
