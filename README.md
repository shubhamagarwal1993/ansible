# ansible

## This is an ansible tutorial to get your server up and running

Why use Ansible:
- Stateless (No background process is running)
- consistency and can be run again and again (Can run the script multiple times on a server)
- Save time next time we need to bring up a new machine, keeping all the settings

#### Components of a functional website
- Setting up a server:
  - Ubuntu 16.04
  - nginx
  - supervisor
  - Domain name (set up on www and *.)
- Deciding on the languages (AWS EC2 t2.micro with static public ip):
  - Backend - php / Haskell / python
  - Frontend - html / css / bootstrap / JQuery / JS / Elm
- Database (but will not use it for now)
- AWS
- load balancers (for multiple DB servers, will not use it now)

### Steps to get a website up and running completely:
- Setting up a server:
  - Set up EC2 on AWS:
    - Make new instance of Ubuntu 16.04
    - Can select lowest instance of EC2
    - For security groups use:
      - ```80 for HTTP, 443 for HTTPS, and 22 for SSH```
    - Create a public / private key pair
      - Name it “web1” -> can call it anything
      - Press “Download Key Pair, a “.pem” file is downloaded
    - Move the file to “~/.ssh/“ folder along with other keys you have. Make sure you pick a different name for your key from the ones in the .ssh folder
    - Now launch instance. It will take a few minutes to start it.
    - To test, we will ssh into the server directly from local computer
      - ```ssh ubuntu@<ip address of EC2>```
      - This will give warning that you have not connected to this server before and you can type yes to this.
      - You should get a permission denied (public key) error at this point
      - Edit “~/.ssh/config" file, and add:
        ```Host web1
			       Hostname <ip of EC2>
    			   IdentityFile ~/.ssh/web1.pem
			       User ubuntu```
      - You can now use ssh web1 from terminal to ssh into server with name of server. You should still be getting a                 permission denied (public key) error
        We get this error because the read permissions of our private key (pem file) are too open. We need to change this to         600 or lower. Lets make it 400
        ```chmod 400 ~/.ssh/web1.pem```
        Now try ssh web1 again and you should be able to ssh into the server
  - Install python on EC2 server (ansible needs python to work - so this step is manual)
    - change to sudo mode
      ```sudo su -```
    - update and upgrade server
      ```apt update && apt upgrade```. 
      - Might have to press 'y' or press enter to continue
      - Might have to update grub -> choose 1st option to upgrade
    - install python (this will install python 2.7, would be better to use 3 at this point)
      ```apt install python```
- Set up ansible (This is on your local computer, or from where you are managing your webservers)
  - Download ansible from “docs.ansible.com"
  - Check ansible version (I had version 2.4.x) using:
    ```anisble —version```
  - Check pinging your localhost to make sure ansible is set up properly (This should return SUCCESS):
    ```ansible all -i ‘localhost,’ -c local -m ping```
  - Now make a file called “hosts” on your desktop and put one line “localhost” in it
  - Now run ```ansible all -i Desktop/hosts -c local -m ping```. This should return SUCCESS. This sets up out inventory
  - Now edit hosts file to read one line ```localhost ansible_connection=local```
  - Run command ```ansible -i Desktop/hosts -m ping```. This should return SUCCESS
  - Now connect to our own server
    - Add this to out host file
      ```web1 ansible_host=52.91.170.213 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/web1.pem```
    - Run ```ansible all -i Desktop/hosts -m ping```. This should return a SUCCESS for both localhost and web1

-------------------------- DONE TILL HERE ------------------------------------
More with ansible



Set up ubuntu
sudo apt-get update
sudo apt-get upgrade
check python version ()
install nom with `sudo apt-get install npm`
Set up nginx
Sdsdsv
Set up gunicorn


We can actually do all this with a single `Ansible script` as below:






check
single page apps
python/django OR python/flask OR php/cakephp OR what  else to use

After the script has finished running:
Check if script has thrown any warnings/errors
Check if all versions are latest
Check if website up by using domain name



front end in html,css,js

backend in python



Using SQL for databases
Use SQL designer; something very basic to design 
Can fork it from here (https://github.com/ondras/wwwsqldesigner)
Can also use it straight on this link (shubham.io/sql)




set up your vim config file (~/.vimrc - will have to be created)
" show line numbers
set number

" Turn on syntax highlighting
syntax on

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab

" highlight word on search
set hlsearch







Architecture to consider:
Frontend:
 - Js, Elm, Html, Css, 

Backend:
 - Nginx, mysql, php/python/haskell, redis

Devops
 - Ansible

Mobile
 - objective c for iOS.




—————————————————
Ansible

Install on macOS
 - brew install ansible

Then navigate to /usr/local/bin and do ls
You will see ansible files there

