# Cloudflare Test Origin

A web application that spits out some random stuff, and asks for status codes.


## Installation

The application supports Ansible which will install all required services, code, and configurations to run on a fresh linux ubuntu system.

NGINX will run on port 80 proxying to the flask app on localhost port 8000 and 8001.

To install just enter these commands:
```
sudo apt install ansible
wget https://raw.githubusercontent.com/jonrankin/cf-test-server/master/cf-server.yml
ansible-playbook cf-server.yml
```
