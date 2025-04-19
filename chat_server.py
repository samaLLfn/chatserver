from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
chat_log = []

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    msg = {
        "user": data.get("user", "anon"),
        "text": data.get("text", ""),
        "time": datetime.now().isoformat()
    }
    chat_log.append(msg)
    # Limit log size
    if len(chat_log) > 100:
        chat_log.pop(0)
    return jsonify({"status": "ok"})

@app.route('/messages', methods=['GET'])
def messages():
    return jsonify(chat_log)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)