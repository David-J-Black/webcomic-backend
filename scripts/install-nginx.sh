#!/bin/bash

script_location=$(dirname "$0")
cd "$script_location/.." || Exit
current_location=$(pwd)
nginx_config_location="$current_location/filesToMoveUponInstallation/nginxWebcomic.conf"
config_destination="/etc/nginx/nginx.conf"

echo "| Installing Nginx...|"

sudo apt install nginx

sudo cp -f "$nginx_config_location" "$config_destination" 

sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx.service 

sudo nginx -s reload
sudo nginx -t

echo "~ Installing frontend Fin ~"
# Error logs at: /var/log/nginx/error.log