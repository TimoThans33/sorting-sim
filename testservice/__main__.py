#!/usr/bin/python3.8

from testservice import app
from testservice.config import *

def main(args=None):
    app.run(host=IP_ADDRESS, port=PORT, debug = True)
if __name__ == "__main__":
    main()