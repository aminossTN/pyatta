#!/usr/bin/python

from flask import Flask, request
import sys
import json
import vyatta


def init_env():
    '''
    Initialize the environment with some params
    '''
    #not yet implemented

app = Flask(__name__)

@app.route('/shutdown', methods = ['POST'])
def shutdown_server():
    '''
    This function is for shutting down the flask web server
    '''
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Pyatta API shutting down...'

@app.route('/api/v1.0/vyatta/intrefaces/<string:type>',methods=['GET'])
def get_vyatta_interfaces(type):
    try:
        output = vyatta.get_interfaces_infos(type)
    except vyatta.ErrorInterafaceType:
        output = {'error':'Network interface type not recognized'}
    return json.dumps(output)

if __name__ == "__main__":

    if sys.argv:
        #Starting server
        if sys.argv[1] == 'start': app.run(host='0.0.0.0', debug = True)
