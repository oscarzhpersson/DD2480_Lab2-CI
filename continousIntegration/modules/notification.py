from itsdangerous import json
import os


def notify(PATH, data):
    SHA = data["after"]
    REPO = data["repository"]["full_name"]
    os.system(f'curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/{REPO}/{SHA} -d "{"state":"success"}" ')

    return "OK"