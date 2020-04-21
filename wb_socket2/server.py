#!/usr/bin/env python

import asyncio
import websockets
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)

  #  Exceptions in the connection handler at the ERROR level
    #Exceptions in the opening or closing handshake at the INFO level
    #All frames at the DEBUG level — this can be very verbose

logger.addHandler(logging.StreamHandler())
async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '192.168.43.254', 6800))
asyncio.get_event_loop().run_forever()