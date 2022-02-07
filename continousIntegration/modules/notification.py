from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(data):
    SHA = str(data["after"])
    REPO = data["repository"]["full_name"]
    GIT_API = "https://api.github.com"
    query = GIT_API + "/repos/" + REPO + "/statuses/" + SHA
    
    # os.system("curl " + "-X POST" + "-H Accept: application/vnd.github.v3+json" + "https://api.github.com/repos/{REPO}/{SHA}" + "-d {'state':'success'}")
    
    response = requests.post(query,
            data = {'state':'pending'})
    print(response.json())
    print(response.headers)

    print("---")

    r = requests.get(GIT_API + "/repos/" + REPO + "/statuses/" + SHA)
    print(GIT_API + "/repos/" + REPO + "/statuses/" + SHA)
    print(r.status_code)
    print(r.json())

    #/repos/{owner}/{repo}/statuses/{sha}

    return "OK"