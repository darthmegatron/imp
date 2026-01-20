#! /usr/bin/env zsh

python3 -m venv venv
pip3 install -r requirements.txt
source venv/bin/activate

clear && echo "To exit the virtual environment use the command 'deactivate'"

