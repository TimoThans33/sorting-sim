#!/usr/bin/env python3
import os
import sys
import time
from sanic import Sanic, response
from jinja2 import Template, FileSystemLoader, Environment

# get environment variables for configuration
static_files_dir = os.getenv('STATIC_FILES_DIR', os.path.join(os.path.dirname(os.path.realpath(__file__)), "static"))

env = Environment(loader=FileSystemLoader(static_files_dir))

app = Sanic(__name__)
app.ws_clients = set()
app.static('static', static_files_dir)

@app.route('/')
async def index(request):
    return response.html( env.get_template("/html/sorting.html").render())
    
if __name__ == "__main__":
    app.run(host="localhost", port=8000)
