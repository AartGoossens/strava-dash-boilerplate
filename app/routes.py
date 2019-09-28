from flask import send_from_directory

from .server import app


@app.server.route('/static/<path>')
def serve_static(path):
    return send_from_directory('static', path)
