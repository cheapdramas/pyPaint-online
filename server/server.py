from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from fastapi.testclient import TestClient
import uvicorn
import asyncio
from connectionmanager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()


@app.websocket('/ws')
async def websocket_endpoint(websocket:WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            
            data = await websocket.receive_text()
            print(data)
            
            
            await websocket.send_text(f'Message text was: {data}')
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    
    except:
        pass
        





if __name__ =='__main__':
    uvicorn.run('server:app',reload=True,port=8000)