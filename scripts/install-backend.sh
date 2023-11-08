#!/bin/bash

echo "__INSTALLING BACKEND__"

echo "---Installing Packages---"
sudo apt -y install nginx unzip

#setup variables
script_directory=$(dirname "$0")
working_directory="$( cd .. )"
cd "$script_directory/.."


# setting up services
echo "---About to setup the backend service---"
sudo cp "filesToMoveUponInstallation/backend.service" /etc/systemd/system/webcomic.service
echo "-- backend service loaded in system folder --"
sudo systemctl daemon-reload
sudo systemctl enable webcomic.service
sudo systemctl restart nginx.service
sudo systemctl restart webcomic.service

git config --global user.email "davidblacktheemployee@gmail.com"
git config --global user.name "David Black"

sudo systemctl status webcomic.service
sudo systemctl status nginx.service

echo "~ Fin ~"