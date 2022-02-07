from itsdangerous import json
import os
import requests
from flask import Flask, request, json

def notify(data, branch):
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])
    GIT_API = "https://api.github.com"
    STATUS = str(data["repository"]["statuses_url"])
    print(STATUS)
    REF = branch
    query_post = GIT_API + "/repos/" + REPO + "/statuses/" + SHA
    query_get = GIT_API + "/repos/" + REPO + "/commits/" + SHA + "/statuses"


    # Create a commit status
    response = requests.post(query_post,
            params = {'state':'success', 'accept':'application/vnd.github.v3+json'})
    print(response.json())
    print(response.headers)
    print("---")

    # Get list of commit status
    r = requests.get(query_get)
    print(r.status_code)
    print(r.json())

    #/repos/{owner}/{repo}/statuses/{sha}

    return "OK"