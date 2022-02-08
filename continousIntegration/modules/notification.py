from wsgiref import headers
from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(data, branch, TOKEN):
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])
    GIT_API = "https://api.github.com"

    query_post = GIT_API + "/repos/" + REPO + "/statuses/" + SHA
    query_get = GIT_API + "/repos/" + REPO + "/commits/" + SHA + "/statuses"

    # Create a commit status using curl
    state = r"\"state\":\"success\"" #"{\"state\": \"failure\" }" #"'state':'failure'"
    #command = f'curl -H "Authorization: token {TOKEN}" "Content-Type: application/json"   -X POST -d "{{state}}" https://api.github.com/repos/{REPO}/statuses/{SHA}'
    command = 'curl -H "Authorization: token ' + TOKEN + '" "Content-Type: application/json"   -X POST -d "{'+ state +'}" https://api.github.com/repos/' + REPO +'/statuses/' + SHA
    print("---")
    print(command)
    print("---")
    os.system(command)

    """response = requests.post(query_post,
            data = {'state':'failure', 'accept':'application/vnd.github.v3+json'}, headers={"Authorization: token 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"})
    print(response.json())
    print(response.headers)
    print("---")"""

    # Get list of commit status
    r = requests.get(query_get)
    print(r.status_code)
    print(r.json())

    return "OK"