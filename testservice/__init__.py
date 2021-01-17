#!/usr/bin/env python3
import os
import sys
import time
from sanic import Sanic, response, Blueprint
from jinja2 import Template, FileSystemLoader, Environment
from sanic.response import json, file
import json
import socket
import random
from datetime import date, datetime

# HOST = '127.0.0.1'
# PORT = 8888

host = '0.0.0.0'
port = 2001

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

test_array = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"
            ,"2","2","2","2","2","2","2","2","2","2"
            ,"3","3","3","3","3","3","3","3","3","3"
            ,"4","4","4","4","4","4","4","4","4","4"
            ,"5","5","5","5","5","5","5","5","5","5"
            ,"6","6","6","6","6","6","6","6","6","6"
            ,"7","7","7","7","7","7","7","7","7","7"
            ,"8","8","8","8","8","8","8","8","8","8"
            ,"9","9","9","9","9","9","9","9","9","9"
            ,"10","10","10","10","10","10","10","10","10","10"
            ,"10"
            ,"9"
            ,"8"
            ,"7"
            ,"6"
            ,"5"
            ,"4"
            ,"3"
            ,"2"
            ,"1"
            ,"1"
            ,"6"
            ,"2"
            ,"7"
            ,"3"
            ,"8"
            ,"4"
            ,"9"
            ,"5"
            ,"10"
]

def testing_func(scanner_id=1, barcode = 4206005698049202090135079104324001, socket=socket):
    for i in test_array:
        direc = i
        zf_dir = i.zfill(3)
        station_id = '\x02MSA-12345-001'
        scanner_id = str(scanner_id) 
        barcode = str(barcode)
        date_str = date.today().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H:%M:%S")
        eos = 'Z\x03'
        message = station_id +","+ scanner_id +","+ zf_dir +","+ barcode +","+ direc +","+ date_str + "T" + time_str + eos
        print(message)
        socket.sendall(bytes(message, 'utf-8'))
        read = socket.recv(1024)
        print(read)
        if read == b"":
            print("no message")
        socket.sendall(bytes(message, 'utf-8'))
        read = socket.recv(1024)
        print(read)
        if read == b"":
            print("no message")
        time.sleep(0.1)


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
            s.connect((host, port))
            while True:
                data = await ws.recv()
                data = json.loads(data)
                barcode_init = barcode_init + 1
                if data["name"][0] == 0:
                    print("start test")
                    testing_func(socket = s)
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
