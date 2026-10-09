from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)


@app.route('/')

def main():
    return ('hello_world')

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname':socket.gethostname()
    })

@app.route('/api/v1/healthz')

def health():
    # Do an actual check here
    return jsonify({'status':'up'}), 200

if __name__ == '__main__':

    app.run()