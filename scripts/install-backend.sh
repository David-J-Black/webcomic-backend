#!/bin/bash

echo "__INSTALLING BACKEND__"
#setup variables
script_directory=$(dirname "$0")
working_directory="$( cd .. )"
cd "$script_directory/.."
pwd

# setting up services
echo "About to setup the backend service"
sudo cp "filesToMoveUponInstallation/backend.service" /etc/systemd/system/webcomic.service
echo "backend service loaded"
sudo systemctl daemon-reload
sudo systemctl enable webcomic.service
sudo systemctl start
sudo systemctl restart nginx.service sudo