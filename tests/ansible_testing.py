#! /usr/bin/env python3

import ansible_runner
from pathlib import Path

def main():
    # Define the directory where your yaml/ini files live
    # Using .resolve() ensures we get the absolute path
    ansible_dir = (Path.cwd() / 'ansible').resolve()

    # Define a separate folder for runner artifacts (logs, status)
    # so we don't clutter your source directory
    artifacts_dir = (Path.cwd() / 'runner_output').resolve()

    r = ansible_runner.run(
        private_data_dir='./ansible',
        playbook=str(ansible_dir / 'test.yaml'),   # Points to ./ansible/test.yaml
        inventory=str(ansible_dir / 'hosts.ini')   # Points to ./ansible/hosts.ini
    )

    print(f"Status: {r.status}")
    print(f"Final RC: {r.rc}")

if __name__ == '__main__':
    main()
