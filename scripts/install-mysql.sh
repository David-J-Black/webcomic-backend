#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y mysql-server

# sudo mysql_secure_installation utility

# MySQL connection parameters
MYSQL_USER="root"
MYSQL_PASSWORD="PeanutButter"
MYSQL_DATABASE="your_database"

# MySQL command to run
# MYSQL_COMMAND="SELECT * FROM your_table;"

# Run the MySQL command
# sudo mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -D "$MYSQL_DATABASE" -e "$MYSQL_COMMAND"

sudo mysql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'PeanutButter69!' WITH GRANT OPTION;
FLUSH PRIVILEGES;