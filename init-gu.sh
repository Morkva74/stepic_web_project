#!/bin/sh
sudo /etc/init.d/gunicorn stop
sudo rm -rf /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/qa.py   /etc/gunicorn.d/qa.py
sudo /etc/init.d/gunicorn start