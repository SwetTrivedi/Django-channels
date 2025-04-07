## Topic Consumer 
## topic Routing
from channels.consumer import SyncConsumer , AsyncConsumer 


class Mysyncconsumer(SyncConsumer):
    #this handler is called when client initially opens a connection and is about
    # to finish the websocket handshake

    def websocket_connect(self,event):
        print("Websocket Connected ")

    # this handler is called when data recieved from client

    def websocket_receive(self,event):
        print("websocket Reccieved")

    # this handler is called when either connection to the client is lost 
    # either closing the connection ,the server closing the connection 

    def websocket_disconnect(self,event):
        print('websocket Disconnct ')



class MyAsyncconsumer(AsyncConsumer):
    #this handler is called when client initially opens a connection and is about
    # to finish the websocket handshake

    async def websocket_connect(self,event):
        print("Websocket Connected ")

    # this handler is called when data recieved from client

    async def websocket_receive(self,event):
        print("websocket Reccieved")

    # this handler is called when either connection to the client is lost 
    # either closing the connection ,the server closing the connection 

    async def websocket_disconnect(self,event):
        print('websocket Disconnct ')