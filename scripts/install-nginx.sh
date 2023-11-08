#!/bin/bash

script_location=$(dirname "$0")
cd ..
current_location=$(pwd)
nginx_config_location="cat filesToMoveUponInstallation/nginxWebcomic.conf"
config_destination="/etc/nginx/nginx.conf"

echo "| Installing Nginx...|"

sudo apt install nginx

sudo cp "$nginx_config_location" "$config_destination" 

sudo systenmctl enable nginx
sudo systenmctl start nginx
sudo systemctl status nginx.service 

sudo nginx -s reload
sudo nginx -t

echo "~ Installing frontend Fin ~"
# Error logs at: /var/log/nginx/error.log