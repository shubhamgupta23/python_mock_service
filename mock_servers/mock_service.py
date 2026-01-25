import json

from flask import Flask

app = Flask(__name__)

@app.route('/health',methods=['GET'])
def health():
    return json.dumps({
        'status': '200 OK',
        'message': 'service is healthy and running'
    }), 200

def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()