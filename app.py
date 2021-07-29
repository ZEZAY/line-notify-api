from flask import Flask, request
from flask_cors import CORS, cross_origin
from line_notify import LineNotify
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    line = LineNotify(request.values['token'])
    
    mode = request.values['mode']
    payload = request.values['payload']
        
    if mode == 'text':
        line.notify_text(payload)
    
    if mode == 'sticker':
        payload.split(',')
        line.notify_sticker(int(payload[0]), int(payload[1]))
        
    if mode == 'picture':
        line.notify_picture(payload)

    return 'all good!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
