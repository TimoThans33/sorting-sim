import asyncio
import time
import random
import socket
from datetime import date, datetime
import sys

def generate_direction(simulation_direction_range):
    direc = str(random.randint(simulation_direction_range[0], simulation_direction_range[1]))
    zf_dir = direc.zfill(3)
    return zf_dir, direc

def compose_msg(scanner_id=1, direction_range=[1,24], barcode = 4206005698049202090135079104324001):
    zf_dir, direc = generate_direction(direction_range)
    station_id = '\x02MSA-12345-001'
    scanner_id = str(scanner_id)
    barcode = str(barcode)
    date_str = date.today().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H:%M:%S")
    eos = 'Z\x03'
    return (station_id +","+ scanner_id +","+ zf_dir +","+ barcode +","+ direc +","+ date_str + "T" + time_str + eos)


async def tcp_echo_client(loop, ip = '192.168.8.2'):
    barcode_init = 4206005698049202090135079104324001
    reader, writer = await asyncio.open_connection(ip, 8888, loop=loop)
    while True:
        barcode_init = barcode_init + 1
        message = compose_msg(barcode = barcode_init)
        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        if (data.decode()==''):
            writer.close()
            reader, write = await asyncio.open_connection(ip, 8888, loop=loop)
        print(f'Received: {data.decode()!r}')
        time.sleep(2)
    print('Close the connection')


if __name__ == "__main__":
    ip = '127.0.0.1'
    # time.sleep(5)
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(tcp_echo_client(loop, ip))

