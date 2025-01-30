import os
from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/info', methods=['GET'])
def get_info():
    
    current_datetime = datetime.now(timezone.utc).isoformat()
    
    data = {
        "email": "uklamido@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/Lamido-stack/task1" 
    }
    
    return jsonify(data), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
