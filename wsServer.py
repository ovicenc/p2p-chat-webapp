from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        print self.data
        for client in clients:
            if client != self:
                client.sendMessage(self.address + u' - ' + self.data)

    def handleConnected(self):
        print self.address, 'connected'
        for client in clients:
            client.sendMessage(self.address + u' - connected')
        clients.append(self)

    def handleClose(self):
        clients.remove(self)
        print self.address, 'closed'
        for client in clients:
            client.sendMessage(self.address + u' - disconnected')

server = SimpleWebSocketServer('', 8080, SimpleChat)
server.serveforever()