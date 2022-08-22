from flask import *

import json, time, sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data = {'Page' : 'Home', 
            'Message' : 'Home page loaded successfully', 
            'Time' : f'@{time.time()}'}

    json_data = json.dumps(data)

    return json_data


@app.route('/request/', methods=['GET'])
def request_page():

    db_command = str(request.args.get('command'))

    data = {'Page' : 'Request', 
            'Message' : f'Successfully received {db_command}', 
            'Time' : f'@{time.time()}',
            'Action' : 'Database extraction started ...'}

    json_data = json.dumps(data)

    return json_data


if __name__ == '__main__':
    app.run(port=7773)
    
