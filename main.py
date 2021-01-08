#!/usr/bin/env python3
import os
import sys
import time
from sanic import Sanic, response, Blueprint
from jinja2 import Template, FileSystemLoader, Environment
from initiate import my_bp
from sanic.response import json, file
import json
import asyncio
import socket
import random
import datetime
from datetime import date, datetime

# HOST = '127.0.0.1'
# PORT = 8888

HOST = '192.168.8.2'
PORT = 2001

# get environment variables for configuration
static_files_dir = os.getenv('STATIC_FILES_DIR', os.path.join(os.path.dirname(os.path.realpath(__file__)), "static"))

env = Environment(loader=FileSystemLoader(static_files_dir))

app = Sanic(__name__)
app.ws_clients = set()
app.static('static', static_files_dir)

# registering route defined by blueprint
# app.blueprint(my_bp)

def generate_direction(simulation_direction_range):
    direc = str(random.randint(simulation_direction_range[0], simulation_direction_range[1]))
    zf_dir = direc.zfill(3)
    return zf_dir, direc


def compose_msg(scanner_id=1, direction_range=[1,24], barcode = 4206005698049202090135079104324001):
    zf_dir,direc = generate_direction(direction_range)
    station_id = '\x02MSA-12345-001'
    scanner_id = str(scanner_id) 
    barcode = str(barcode)
    # barcode = '4206005698049202090135079104324001'
    date_str = date.today().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H:%M:%S")
    eos = 'Z\x03'
    return (station_id +","+ scanner_id +","+ zf_dir +","+ barcode +","+ direc +","+ date_str + "T" + time_str + eos)

@app.route('/')
async def index(request):
    return response.html( env.get_template("/html/sorting.html").render())
    
@app.route('/config')
async def index(request):
    return response.html( env.get_template("/html/config.html").render())

@app.route('/advanced')
async def index(request):
    return response.html( env.get_template("/html/advanced.html").render())

@app.route('/websocket')
async def test(request):
    return response.html( env.get_template("/html/websocket.html").render())

@app.websocket('/feed')
async def feed(request, ws):
    print("request")
    barcode_init = 4206005698049202090135079104324001
    # reader, writer = await asyncio.open_connection(ip, port)
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                data = await ws.recv()
                data = json.loads(data)
                barcode_init = barcode_init + 1
                message = compose_msg(barcode = barcode_init, direction_range=[int(data["name"][0]),int(data["name"][1])])
                print("send : ",message)
                s.sendall(bytes(message, 'utf-8'))
                read = s.recv(1024)
                print(read)
                if read == b"":
                    print("no message")
                    break
            print("restarting socket...")
        # writer.write(message.encode())
        # print(data)
        # data = json.loads(data)
        # print(data["name"][0])

if __name__ == "__main__":
    # ip = sys.argv[1]
    # port = sys.argv[2]
    # print("test")
    # start_server = websockets.serve(websocket, ip, port)
    
    # asyncio.get_event_loop().run_until_complete(start_server)
    # asyncio.get_event_loop().run_forever()
    # print("test")
    app.run(host='192.168.8.231', port=6543, debug = True)