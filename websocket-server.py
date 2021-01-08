import asyncio
import websockets
import datetime
import random
import sys

# websocket server example 

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)


ip = sys.argv[1]
port = sys.argv[2]

start_server = websockets.serve(time, ip, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

