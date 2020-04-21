import asyncio
import json
import logging
import websockets
import ssl
import pathlib

logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)

logging.basicConfig()
USERS = set()


async def register(websocket):
    USERS.add(websocket)
    # await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)


async def deploy_service(websocket, path):
    await register(websocket)
    try:
        # await websocket.send()
        async for message in websocket:
            data = json.loads(message)
            print(data)
            await websocket.send('data received')
    finally:
        await unregister(websocket)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(deploy_service, '192.168.43.254', 6800, ssl=ssl_context)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()