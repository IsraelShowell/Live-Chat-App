# Creator: Israel Showell
# Start Date: 4/10/2024
# End Date: 4/10/2024
# Project: Live-Chat-Room
# Version: 1.00

# Description:

"""
This is a basic live chat program that allows multiple users to talk to one another
via the UI. The base code was created by @arpanneupane19.
https://github.com/arpanneupane19/python-socketio-app-youtube

I plan on expanding upon this code, and combining my login/register
Flask application with this code. 
This project is a way for me to practice Flask development, linking HTML/CSS Front-End to Python Back-End,
and Live-Chat Functionailty.

Practiced Skills:

- Practicing POST and GET Requests and Socket Opening Between Users
- Connecting Front-Ends and Back-Ends together
- Developing Web Applications

"""

from flask import Flask, render_template

"""
Sockets establish a path through
which one computer can interact with the other.
It can be considered as a gate
which enables the communication only if the gates are open,
i.e only if the socket’s open.

SocketIO is a cross-browser Javascript library that abstracts the
client application from the actual transport protocol.
SocketIO, that any browser out there will be able to connect to
the application.
"""

"""
flask-socketio creates sockets for Flask.
Flask-SocketIO gives flask applications access to bi-directional communications
between the clients and the server.
The client-side application can use any of the SocketIO official client
libraries in Javascript, C++, Java and Swift,
or any compatible client to establish a permanent connection to the server.
"""

from flask_socketio import SocketIO, send


#Important variables and objects
#Requried by Flask to detect the app when running 'flask run'
# Initialize Flask application
app = Flask(__name__)

#This is used to help protect data being sent by the app.
#This protection is used to defend against CSRF attacks.
#(Cross-Site Request Forgery)
app.secret_key="__privatekey__"

# Initialize SocketIO with the Flask app
socketio = SocketIO(app)

@app.route('/')
def index():
    # Calls the HTML page that contains the Socket.IO client
    return render_template('message.html')

# Handles events for the 'message' event
@socketio.on('message')

def handle_message(message):
    # This function is called when the client sends a message
    print('Received message:', message)
    # Echos the message back to the client
    socketio.emit('message', message)

if __name__ == '__main__':
    # Starts the Flask application along with Socket.IO
    socketio.run(app)

