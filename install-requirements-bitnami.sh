#!/bin/bash

# Sources:
# https://flask.palletsprojects.com/en/2.3.x/deploying/mod_wsgi/

current_location=$(dirname "$0")
requirements_location="$current_location/requirements.txt"
nginx_config_destination="/opt/bitnami/nginx/conf/nginx.conf"

# Install our requirements
# - Angy because i'll install this copy of python3.11 and it says I'm running 3.10.3 >:(
sudo apt install -y python3  python3-pip python3-venv unzip

python3 -m venv venv
sudo chmod -R +rwx venv

# Setup the apache folder for the frontend
sudo mkdir -p /var/www/frontEnd
sudo chown -R $USER:$USER /var/www/frontEnd
sudo chmod -R 755 /var/www

# Install backend
sudo bash scripts/install-backend.sh

# Copy the configs to the folder where apache configs go idfk
sudo cp filesToMoveUponInstallation/nginxWebcomic.conf /etc/nginx/nginx.conf
# Why is apache running? We're using nginx bitch!

# Activate our python venv then install all the crap the server
# Needs to run
# We want our server to be a healthy boy
# Feed her all the juicy libraries

source venv/bin/activate
pip3 install -r requirements.txt
deactivate