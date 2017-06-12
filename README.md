“огда при решении очередного задани€ необходимые действи€ будут сведены к минимуму:

git clone https://github.com/Morkva74/stepic_web_project /home/box/web
bash /home/box/web/init.sh

python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('user1', '', '1')
user.save()