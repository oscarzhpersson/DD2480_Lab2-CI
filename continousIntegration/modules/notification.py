import os
from flask import Flask, json

def notify(data, STATUS, TOKEN):
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])

    # Create a commit status using curl
    state = fr"\"state\":\"{STATUS}\"" 
    command = 'curl -H "Authorization: token ' + TOKEN + '" "Content-Type: application/json"   -X POST -d "{'+ state +'}" https://api.github.com/repos/' + REPO +'/statuses/' + SHA
    os.system(command)

    return "OK"