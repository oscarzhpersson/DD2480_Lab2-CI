from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(data):
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])
    GIT_API = "https://api.github.com"
    REF = str(data["ref"])
    query_post = GIT_API + "/repos/" + REPO + "/statuses/" + SHA
    query_get = GIT_API + "/repos/" + REPO + "/commits/" + REF + "/statuses"
    
    # os.system("curl " + "-X POST" + "-H Accept: application/vnd.github.v3+json" + "https://api.github.com/repos/{REPO}/{SHA}" + "-d {'state':'success'}")
    
    response = requests.post(query_post,
            data = {'state':'pending'})
    print(response.json())
    print(response.headers)
    print("---")

    #/repos/{owner}/{repo}/commits/{ref}/statuses
    r = requests.get(query_get)
    print(r.status_code)
    print(r.json())

    #/repos/{owner}/{repo}/statuses/{sha}

    return "OK"