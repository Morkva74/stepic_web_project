sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/dj.conf /etc/gunicorn.d/dj.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
#sudo service mysql restart
sudo mysql -uroot -e "CREATE DATABASE ask ;"
sudo mysql -uroot -e "CREATE USER 'user1'@'localhost' IDENTIFIED BY '1';"
sudo mysql -uroot -e "GRANT ALL ON ask.* TO 'user1'@'localhost';"
#~/web/ask $ python manage.py makemigrations
#~/web/ask $ python manage.py migrate