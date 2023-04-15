

#!/bin/bash
#cd ..
source env/bin/activate

#cd django-cicd/
echo "working diewsteroy is ##################################"
echo "$PWD"
python3 manage.py makemigrations
python3 manage.py migrate
#python manage.py collectstatic -- no-input
python3 manage.py runserver 0.0.0.0:80

echo "Migrations done"


#cd /var/lib/jenkins/workspace/django-cicd
sudo cp -rf gunicorn.socket /etc/systemd/system/
sudo cp -rf gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"



sudo systemctl daemon-reload
sudo systemctl start gunicorn

echo "Gunicorn has started."

sudo systemctl enable gunicorn

echo "Gunicorn has been enabled."

sudo systemctl restart gunicorn


sudo systemctl status gunicorn
