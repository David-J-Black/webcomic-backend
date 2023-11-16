#!/bin/bash

# Going off these instructions: https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

echo "__GETTING SSL CERTIFICATION__"

echo "---Certbot installation setup---"
sudo snap install --classic certbot

# Installing cerbot command
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Setup cerbot for nginx
sudo certbot --nginx

# Tell cerbot to renew ssl automatically
sudo certbot renew --dry-run

## Certbot installs in one of the following locations ##
# /etc/crontab/
# /etc/cron.*/*
# systemctl list-timers