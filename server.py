import os
from flask import Flask, request, jsonify, send_from_directory
from config import ADMIN_PASSWORD, PORT, CHANNEL_ID
from bot import upload_to_telegram

app = Flask(__name__, static_folder=".")
hosted_files = []

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files: return jsonify({"success": False}), 400
    file = request.files['file']
    path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(path)
    file_id, msg_id = upload_to_telegram(path)
    if os.path.exists(path): os.remove(path)
    if file_id:
        clean_id = str(CHANNEL_ID).replace("-100", "")
        link = f"https://t.me/c/{clean_id}/{msg_id}"
        hosted_files.append({"name": file.filename, "link": link})
        return jsonify({"success": True, "link": link})
    return jsonify({"success": False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
  
