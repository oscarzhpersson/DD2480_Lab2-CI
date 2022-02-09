import os
from flask import Flask, json

def notify(data, STATUS, TOKEN):
    ''' Will set commit status to 'pending', 'success' or 'failure' based on STATUS input. The status set will be visible on GitHub in the commit history after a push.

        Parameters
        ----------
        data: JSON file containing webhook payload.
        STATUS: Set by caller to 'pending', 'success', 'failure' or other valid statuses.
        TOKEN: Set by caller to authenticate in order to make GitHub API calls.

    '''
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])

    if not TOKEN:
        raise ValueError('No authorization token is provided')

    # Create a commit status using curl
    state = fr"\"state\":\"{STATUS}\"" 
    command = 'curl -H "Authorization: token ' + TOKEN + '" "Accept: application/vnd.github.v3+json" -X POST -d "{'+ state +'}" https://api.github.com/repos/' + REPO + '/statuses/' + SHA
    os.system(command)