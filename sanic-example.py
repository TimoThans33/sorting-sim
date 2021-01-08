from sanic import Sanic
from sanic.response import file

app = Sanic(__name__)

@app.route("/")
async def test(request):
    return await file('websocket.html')

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)
        
if __name__ == "__main__":
    app.run(host="localhost", port=8000)
