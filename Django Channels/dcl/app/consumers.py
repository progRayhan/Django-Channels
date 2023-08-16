from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("websocket connected...")
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print("Message Received from client...", type(event))
        print(f"client message is: ", event['text'])

    def websocket_disconnect(self, event):
        print("Websocket disconnect...")
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("websocket connected...")
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Message Received from client...")
        print("Client message: ", event['text'])

    async def websocket_disconnect(self, event):
        print("Websocket disconnect...")
        raise StopConsumer()
    
