
from flask import *

import json, datetime as dt, sys, time
from threading import Thread

app = Flask(__name__)


def get_db_data():
    for i in range(5):

        time.sleep(2)
    print('DONE')
    return json.dumps({'Status':'Data extraction DONE'})

t1 = Thread(target=get_db_data)

@app.route('/', methods=['GET'])
def home_page():
    data = {'Page' : 'Home', 
            'Message' : 'Home page loaded successfully', 
            'Time' : f'@{dt.datetime.now()}'}

    json_data = json.dumps(data)

    return json_data




@app.route('/overview/', methods=['GET'])
def request_page():

    data = {'Page' : 'Overview', 
            'Message' : 'This is the overview page', 
            'Time' : f'@{dt.datetime.now()}'
            }

    json_data = json.dumps(data)

    return json_data

@app.route('/overview/request/', methods=['GET'])
def execute():
    db_command = str(request.args.get('command'))
    output = {'Command' : f'{db_command}'}

    if (db_command == 'get') or (db_command == 'GET'):

        output.update({'Execution' : f' of {db_command} @ {dt.datetime.now()}' })
        
        t1.start()
    
    output = json.dumps(output)

    return output


if __name__ == '__main__':
    app.run(port=7773)
    
