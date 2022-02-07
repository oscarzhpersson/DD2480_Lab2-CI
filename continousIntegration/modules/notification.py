from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(REPO, NAME, data):
    SHA = data["after"]
    #REPO = data["repository"]["full_name"]
    GIT_API = "https://api.github.com"
    
    # os.system("curl " + "-X POST" + "-H Accept: application/vnd.github.v3+json" + "https://api.github.com/repos/{REPO}/{SHA}" + "-d {'state':'success'}")
    
    r = requests.post(GIT_API + "/repos/" + NAME + "/" + REPO + "/statuses/" + SHA)
    print(r.text)

    #/repos/{owner}/{repo}/statuses/{sha}

    return "OK"