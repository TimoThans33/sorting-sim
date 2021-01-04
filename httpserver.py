from BaseHTTP import BaseHTTPRequestHandler, HTTPServer
import os
# Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):
        rootdir = 'c:/xamp'