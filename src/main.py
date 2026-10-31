from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, jsonify

msk_tz = ZoneInfo("Europe/Moscow")
app = Flask(__name__)


@app.route("/ping")
def hello_world():
    return jsonify(
        {"message": "pong", "timestamp": datetime.now(tz=msk_tz).isoformat()}
    )
