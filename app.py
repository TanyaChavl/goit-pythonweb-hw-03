from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__, static_folder='static')
DATA_FILE = 'storage/data.json'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form.get('username')
        message_text = request.form.get('message')
        timestamp = str(datetime.now())

        data = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}

        data[timestamp] = {
            "username": username,
            "message": message_text
        }

        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)

        return redirect(url_for('read'))

    return render_template('message.html')


@app.route('/read')
def read():
    messages = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = {}
    return render_template('read.html', messages=messages)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)