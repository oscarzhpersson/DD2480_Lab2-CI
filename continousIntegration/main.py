##### IMPORTS #####

from flask import Flask, request, json

##### SETTINGS #####

STATUS_DEBUG = True
HOST = "127.0.0.1"
PORT = 5000

##### PROGRAM #####

app = Flask(__name__) # Variable for flask server application, to be called upon.

# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    data = request.json # Request the data from the event.

    print("Received PUSH event from webhook!") # Debug print.

    # TODO: Extract Repository.
    # TODO: Save relevant parts of repo into variables to send to the other scripts.

    branch = None

    # Here you do all the continuous integration tasks
    # For example:
    # 1st clone your repository
    # 2nd compile the code

    #Flask.Response(status=200)
    return "OK" # Defaults to 200 response code.


# Start the Flask web server.
if __name__ == '__main__':
    app.run(debug=STATUS_DEBUG, host=HOST, port=PORT)