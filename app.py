from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/locate', methods=['POST'])
def locate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid or missing JSON'}), 400

        response = requests.post(
            'https://location.services.mozilla.com/v1/search?key=test',
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )

        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to reach MLS service', 'details': str(e)}), 502
    except Exception as ex:
        return jsonify({'error': 'Internal server error', 'details': str(ex)}), 500

if __name__ == '__main__':
    app.run()
