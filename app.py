from flask import Flask, jsonify\napp = Flask(__name__)\n@app.route('/')\ndef hi():\n    return jsonify(msg='Hi')
