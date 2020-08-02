#!/bin/bash

echo "Installing dependencies..."
add-apt-repository universe
apt update

echo "Installing nginx..."
apt install nginx -y

echo "Installing let's encrypt..."
apt install software-properties-common -y
apt install certbot python3-certbot-nginx -y

echo "Installing python dependencies..."
apt install python3-pip -y
apt install python3-dev -y
apt install python3-venv -y
apt install python3-wheel -y
pip3 install wheel

echo "Installing Docker..."
# https://docs.docker.com/engine/install/ubuntu/
apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt update
apt install docker-ce docker-ce-cli containerd.io -y

echo "Installling Docker Compose..."
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "Installing dplhooks..."
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 scripts/config.py

echo "Preparing gunicorn..."
cp scripts/.tmp/dplhooks.service /etc/systemd/system/dplhooks.service
systemctl daemon-reload
systemctl start dplhooks
systemctl enable dplhooks
systemctl status dplhooks

echo "Preparing nginx..."
cp scripts/.tmp/nginx-site-dplhooks /etc/nginx/sites-available/dplhooks
ln -s /etc/nginx/sites-available/dplhooks /etc/nginx/sites-enabled
systemctl restart nginx

cp scripts/.tmp/sudoers-dplhooks /etc/sudoers.d/dplhooks

certbot --nginx
systemctl restart dplhooks
