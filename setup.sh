#! /usr/bin/env zsh

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

clear && echo "To exit the virtual environment use the command 'deactivate'"

