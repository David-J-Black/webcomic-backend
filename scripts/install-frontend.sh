#!/bin/bash

echo "- Installing Webcomic frontend...-"

# setup variables
script_directory=$(dirname "$0")
cd "$script_directory/.." || exit
base_location=$(pwd)

location_of_zip="$base_location/filesToMoveUponInstallation/package.zip"
frontend_from_zip="dist/webcomic-frontend/*"
destination_of_unzip="dist"
nginx_serve_folder="/var/www"

# Setup the apache folder for the frontend
sudo unzip -o $location_of_zip
sudo cp -r -f $frontend_from_zip $nginx_serve_folder
sudo mkdir -p /var/www
sudo chown -R www-data:www-data /var/www

# Move all the necessary files
sudo rm -R -f dist

# Directories (recursively) - execute permissions
sudo find /var/www -type d -exec chmod 755 {} \;

# Files (recursively) - readonly permissions
sudo find /var/www -type f -exec chmod 644 {} \;
echo "~ Installing frontend Fin ~"