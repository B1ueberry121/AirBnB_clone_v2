#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
# Installs Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
#creates a folder if it dosent exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# Creates a fake html file to test the configurations of nginx
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
#Creates a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Changes the owner
sudo chown -hR ubuntu:ubuntu /data/
# Updates the nginx conf
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restarts Nginx
sudo service nginx start
