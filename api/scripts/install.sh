#!/usr/bin/env bash
# Dependencies for this project. Requires Python 3+

pip3 check
pip3 install --upgrade pip
pip3 install boto3 django setuptools

# assume manage.py is in current directory...
python3 manage.py runserver
