##### IMPORTS #####

from flask import Flask, request, json
import logging

##### PROGRAM #####

app = Flask(__name__)

@app.route('/') # Triggered by URL localhost:5000/
def default():
    return "Server up and running"


# Create an endpoint which receives requests from the GitHub API.

@app.route('/githubPush', methods=['POST']) # Triggered by URL localhost:5000/githubPush.
def handler_Push():

    data = request.json # Request the data from the event.

    app.logger.info("Received PUSH event from webhook!") # Debug print.

    return data

if __name__ == '__main__':
    app.run(debug=True)