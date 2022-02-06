##### IMPORTS #####

from flask import Flask, request, json
import logging

##### SETTINGS #####

STATUS_DEBUG = True
HOST = "127.0.0.1"
PORT = 5000

##### PROGRAM #####

app = Flask(__name__)

# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    data = request.json # Request the data from the event.

    app.logger.info("Received PUSH event from webhook!") # Debug print.

    return "OK" #Flask.Response(status=200)



if __name__ == '__main__':
    app.run(debug=STATUS_DEBUG, host=HOST, port=PORT)






##### Things that DID NOT work #####

#@app.route('/githubPush', methods=['POST']) # Triggered by URL localhost:5000/githubPush.
#def default():
#    return "Server up and running"