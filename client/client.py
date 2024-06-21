import websockets
import asyncio
import threading
import time
async def listen():
    
    async with websockets.connect('ws://127.0.0.1:8000') as ws:
            
            
            
        
        a = await ws.send('penis')
        b = await ws.recv()
        print(b)
threading.Thread(target=asyncio.run,args=(listen(),)).start()

