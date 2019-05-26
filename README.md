# Ansible - setup your server

### Why use Ansible
 - Stateless: No background process is running
 - Consistency: Can run the script multiple times, it will not change the server if not needed
 - Save time when you want to bring up a new machine again

## Steps:
 - Step 1: Setup EC2 (AWS) with Ubuntu 18.04
 - Step 2: Setup Ansible on your local computer
 - Step 3: Setup your server
 - Step 4: Additional things that can be added to the script

#### EC2 setup
 - For security groups use `80 for HTTP`, `443 for HTTPS`, and `22 for SSH`
 - Put the `.pem` file in folder `~/.ssh`
 - To test, ssh into the server directly using `ssh ubuntu@<ip address of EC2>`
   - This will give warning that you have not connected to this server before and you can type `yes` to this. You should get a permission denied (public key) error at this point
   - Edit `~/.ssh/config` file, and add:
      ```
      Host web1
          Hostname <ip of EC2>
          IdentityFile ~/.ssh/web1.pem
          User ubuntu
      ```
 - You can now use `ssh web1` from terminal to ssh into the server.
   - You should still be getting a permission denied (public key) error, because the read permissions of our `*.pem` file are too open. We need to change this to `600 or lower`. Lets make it `400` using `chmod 400 ~/.ssh/web1.pem`
   - Now you should be able to ssh
 - Install python on EC2 server (ansible needs python to work - so this step is manual). This may however not be needed with Ubuntu18.04

#### Ansible setup on local machine
 - Install Ansible
   - macOS: use `brew install ansible`
   - Linux: download from `docs.ansible.com`
 - Check version using `anisble —version`, must be 2.4x or higher
 - Download ansible script from github, you should get the `host` and other files.
 - Check ansible setup by pinging your localhost using `ansible all -i ‘localhost,’ -c local -m ping`. This should return SUCCESS
 - Check script setup using `ansible all -i Desktop/hosts -c local -m ping`

#### Setup server
 - Add our server to the script
   - Edge the host file and edit the server configuration to put your own server, something like
   ```
      web1 ansible_host=52.91.170.213 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/web1.pem```
   ```
 - Setup the server by running `clear && ansible-playbook -i hosts init-webserver.yml`. This will take some time, and will show you the steps its working on, as well as SUCCESS or FAILURE
 - Now go the `<ip address>` and you will see a basic web template up.
   - You can ssh in manually and edit the code, or make changes to scripts as needed.

#### More about script
 - The script sets up the following things
   - nginx
   - vim editing tools

#### Other components that can be added to the script
 - supervisor
 - Deciding on the languages (AWS EC2 t2.micro with static public ip):
   - Backend - php / Haskell / python / Nginx / mysql / redis
   - Frontend - html / css / bootstrap / JQuery / JS / Elm
   - Mobile - objective c for iOS
 - Database (but will not use it for now)

#### Manual steps
 - Domain name (setup on www and *.)
 - load balancers (for multiple DB servers, will not use it now)

### Other tools to suppliment your website
 - Database (posegresql or sql) design tool `SQL designer` to design something basic. You can form it from `https://github.com/ondras/wwwsqldesigner`, or use it directly on `https://shubhamagarwal1993.github.io/sql/`
