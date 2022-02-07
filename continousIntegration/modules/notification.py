from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(PATH, data):
    SHA = data["after"]
    print(SHA)
    REPO = data["repository"]["full_name"]

    # os.system("curl " + "-X POST" + "-H Accept: application/vnd.github.v3+json" + "https://api.github.com/repos/{REPO}/{SHA}" + "-d {'state':'success'}")
    
    r = requests.get()

    #/repos/{owner}/{repo}/statuses/{sha}

    return "OK"