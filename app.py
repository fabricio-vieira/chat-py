from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/open_chat', methods=['GET'])
def chat():
	return render_template('index.html', host="http://127.0.0.1:5000")

@socketio.on('connect')
def handle_connect():
      print("Client connected to the server")

@socketio.on('message')
def handle_message(msg):
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)