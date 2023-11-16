#!/bin/bash

script_location=$(dirname "$0")
cd "$script_location/.." || Exit
current_location=$(pwd)
nginx_config_location="$current_location/filesToMoveUponInstallation/nginxWebcomic.conf"

echo "| Installing Nginx...|"

sudo apt install nginx

echo 'Moving nginx file...'
# sudo cp filesToMoveUponInstallation/nginxWebcomic.conf /etc/nginx/nginx.conf
sudo cp -f "$nginx_config_location" /etc/nginx/nginx.conf


sudo systemctl enable nginx
sudo systemctl restart nginx
sudo systemctl status nginx.service 

sudo nginx -s reload
sudo nginx -t

echo "~ Installing frontend Fin ~"
# Error logs at: /var/log/nginx/error.log