##### IMPORTS #####

from flask import Flask, request, json
import logging

##### PROGRAM #####

app = Flask(__name__)

# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    data = request.json # Request the data from the event.

    app.logger.info("Received PUSH event from webhook!") # Debug print.

    return "OK" #Flask.Response(status=200)



if __name__ == '__main__':
    app.run(debug=True)






##### Things that DID NOT work #####

#@app.route('/githubPush', methods=['POST']) # Triggered by URL localhost:5000/githubPush.
#def default():
#    return "Server up and running"