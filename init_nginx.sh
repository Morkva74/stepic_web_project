#!/bin/sh
sudo /etc/init.d/nginx stop
sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx start