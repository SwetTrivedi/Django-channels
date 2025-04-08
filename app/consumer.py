## Topic Consumer 
## topic Routing
from channels.consumer import SyncConsumer , AsyncConsumer 


# class Mysyncconsumer(SyncConsumer):
#     #this handler is called when client initially opens a connection and is about
#     # to finish the websocket handshake

#     def websocket_connect(self,event):
#         print("Websocket Connected " , event)
#         self.send({
#             'type':'websocket.accept'
#         })

#     # this handler is called when data recieved from client

#     def websocket_receive(self,event):
#         print("websocket Reccieved",event)

    # this handler is called when either connection to the client is lost 
    # either closing the connection ,the server closing the connection 

    # def websocket_disconnect(self,event):
    #     print('websocket Disconnct ')



# class MyAsyncconsumer(AsyncConsumer):
#     #this handler is called when client initially opens a connection and is about
#     # to finish the websocket handshake

#     async def websocket_connect(self,event):
#         print("Websocket Connected ")

#     # this handler is called when data recieved from client

#     async def websocket_receive(self,event):
#         print("websocket Reccieved")

#     # this handler is called when either connection to the client is lost 
#     # either closing the connection ,the server closing the connection 

#     async def websocket_disconnect(self,event):
#         print('websocket Disconnct ')


from time import sleep
from channels.exceptions import StopConsumer
class Mysyncconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket Connected ...',event)
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self,event):
        print('Mwssage recieved from client ',event)
        print(event['text'])
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':'Messages Sent to client' , 
                'text':str(i)
            })
            sleep(1)
    def websocket_disconnect(self,event):
        print('websocket disconnect ......', event)
        raise StopConsumer()
        

import asyncio
from channels.exceptions import StopConsumer
class MyAsyncconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Websocket Connected ...',event)
        await self.send({
            'type':'websocket.accept',
        })
    async def websocket_receive(self,event):
        print('Mwssage recieved from client ',event)
        print(event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':'Messages Sent to client' , 
                'text':str(i)
            })
            await asyncio.sleep(1)
        # await self.send({
        #     'type':'websocket.send',
        #     'text':'Messages Sent to client'  
        # })
    async def websocket_disconnect(self,event):
        print('websocket disconnect ......', event)
        raise StopConsumer()