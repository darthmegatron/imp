#!/usr/bin/env python3

import portal_functions as pf
import json
import requests
import json
import csv
import subprocess
from urllib.parse import urljoin
from sys import argv
from pathlib import Path


#script_host = subprocess.run('hostname', stdout=subprocess.PIPE, text=True).stdout.strip()
if Path('/var/lib/transport-api/api-key.json').exists():
    key_path = Path('/var/lib/transport-api/api-key.json')
else:
    key_path = Path.home() / "Documents" / "api-key.json"

with key_path.open() as f:
    key_data = json.load(f)
    api_key = key_data["api_key"]
    username = key_data["username"]
    password = key_data["password"]

request_session = requests.Session()
request_session.mount(pf.Component.BASE_URL, requests.adapters.HTTPAdapter())
request_session.params = {"key": api_key}
login = {"user_id": username, "password": password}
response = request_session.post(urljoin(pf.Component.BASE_URL, "oauth/token"), json=login)
response.raise_for_status()
val = response.json()
request_session.headers["Authorization"] = f"Bearer {val['token']}"
url = urljoin(pf.Component.BASE_URL, "leaves")


def deploy_software(target:str) -> list:
    """Gather software requirements from the portal and deploy them to the appliance(s)."""

    software_list_frontend = ['-f']
    endpoint_info = pf.Endpoint(target, request_session).get_info()['endpoints'][0]
    appliances = pf.Appliances(target, request_session, 'endpoint_id').get_info()['appliances']
    leaves = pf.Leaf(target, request_session, 'endpoint_id').get_info()

    front_ends = []
    deployment_targets = {}

    for x in range(len(appliances)):
        front_ends.append(appliances[x]['appliance_id'])

    if endpoint_info['redundant']:
        software_list_frontend.append('s')

    if any('8' in leaf['tag_ids'] for leaf in leaves):
        software_list_frontend.append('a')

    print(''.join(software_list_frontend))
    print(software_list_frontend)

#print(pf.Hardware(argv[1], request_session, 'endpoint_id').get_info()
#deploy_software(argv[1])

print(pf.Flowclient(argv[1], request_session, "endpoint_id").get_info())

