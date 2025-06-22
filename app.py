from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/locate', methods=['POST'])
def locate():
    try:
        data = request.json
        resp = requests.post(
            'https://location.services.mozilla.com/v1/search?key=test',
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
