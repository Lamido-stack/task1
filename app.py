from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/api/info', methods=['GET'])
def get_info():
    
    current_datetime = datetime.now(timezone.utc).isoformat()
    
    data = {
        "email": "uklamido@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/yourusername/your-repo" 
    }
    
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
