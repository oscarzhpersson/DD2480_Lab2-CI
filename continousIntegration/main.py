##### IMPORTS #####

from flask import Flask, request, json

##### PROGRAM #####

app = Flask(__name__)

@app.route('/') # Triggered by URL localhost:5000/
def default():
    return "Server up and running"

if __name__ == '__main__':
    app.run(debug=True)


# Create an endpoint which receives requests from the GitHub API.

@app.route('/githubPush', methods=['POST']) # Triggered by URL localhost:5000/githubPush
def handler_Push():
    data = request.json

    print("Tests if webhook event is received.")

    return "Tests if webhook event is received."