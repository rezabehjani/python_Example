#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import threading
import time
import secrets
import sys
import socket
import selectors
import types
import time
import datetime
import random
import http
host = "192.168.43.254"
port = 6500
sel = selectors.DefaultSelector()

STATE = {"value": 0}

USERS = set()
web_socket_obj = asyncio.get_event_loop()


logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logging.basicConfig()


def start_connections(connid,messe):
    messages = []
    messages.append(messe.encode("utf-8"))

    server_addr = (host, port)
    print("starting connection", connid, "to", server_addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
        connid=connid,
        msg_total=sum(len(m) for m in messages),
        recv_total=0,
        messages=list(messages),
        outb=b"",
    )
    sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    try:
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                print("received", repr(recv_data), "from connection", data.connid)
                for user in USERS:
                    print("rrrrrrrrrrrrrrr")
                    asyncio.run(user.send(repr(recv_data)))

                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data.msg_total:
                print("closing connection", data.connid)
                sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print("sending", repr(data.outb), "to connection", data.connid)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    except IOError as error:
        print(error)

        print("IOError for service connection ")
        sel.unregister(sock)
        sock.close()


    except UnicodeDecodeError as error:
        print(error)
        sel.unregister(sock)
        sock.close()


    except AttributeError as error:
        print(error)
        sel.unregister(sock)
        sock.close()


    except ValueError as error:
        print(error)
        sel.unregister(sock)
        sock.close()

def init():
    try:
        while True:
            events = sel.select(timeout=None)
            if events:
                for key, mask in events:
                    service_connection(key, mask)
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except IOError as error:
        print(error)
        pass


    except UnicodeDecodeError as error:
        print(error)
        pass


    except AttributeError as error:
        print(error)
        pass


    except ValueError as error:
        print(error)
        pass

    finally:
        print("select .close crash")
        sel.close()





t1 = threading.Thread(target=init)
t1.start()



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
async def health_check(path, request_headers):
    if path == "/health/":
        return http.HTTPStatus.OK, [], b"OK\n"


async def handler_web_socket(websocket, path):
    # register(websocket) sends user_event() to websocket

    await register(websocket)

    try:
        await websocket.send(state_event())

        async for message in websocket:
            print(message)
            id = secrets.token_hex(15)
            start_connections(id, message)

    finally:
        print("reza")
        await unregister(websocket)


start_server = websockets.serve(handler_web_socket, "192.168.43.254", 6800,process_request=health_check)



web_socket_obj.run_until_complete(start_server)

web_socket_obj.run_forever()












