#!/bin/bash

git pull
source venv/bin/activate
pip3 install -r requirements.txt
systemctl restart dplhooks
