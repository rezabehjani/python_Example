# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)

  #  Exceptions in the connection handler at the ERROR level
    #Exceptions in the opening or closing handshake at the INFO level
    #All frames at the DEBUG level — this can be very verbose

logger.addHandler(logging.StreamHandler())


async def time(websocket, path):
    while True:

        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "192.168.43.254", 6800)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()