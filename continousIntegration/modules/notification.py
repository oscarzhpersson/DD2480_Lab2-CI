import os
from flask import Flask, json

def notify(data, STATUS, TOKEN):
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])

    if not TOKEN:
        raise ValueError('No authorization token is provided')

    # Create a commit status using curl
    state = fr"\"state\":\"{STATUS}\"" 
    command = 'curl -H "Authorization: token ' + TOKEN + '" "Accept: application/vnd.github.v3+json" -X POST -d "{'+ state +'}" https://api.github.com/repos/' + REPO + '/statuses/' + SHA
    os.system(command)
		
    return "OK"