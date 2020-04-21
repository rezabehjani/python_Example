#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import threading
import time
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)

  #  Exceptions in the connection handler at the ERROR level
    #Exceptions in the opening or closing handshake at the INFO level
    #All frames at the DEBUG level — this can be very verbose

logger.addHandler(logging.StreamHandler())


logging.basicConfig()

STATE = {"value": 0}

USERS = set()

def send_queu():
    while True:
        time.sleep(1)
        print("reza")
        print(USERS)
        for user in USERS:
            user.send("message")


def state_event():
    return json.dumps({"type": "state", **STATE})



def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):

    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    print(websocket)
    t1 = threading.Thread(target=send_queu)
    t1.start()

    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "192.168.43.254", 6800)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()