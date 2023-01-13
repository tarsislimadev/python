import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 80))
server.listen()

def handle(client, address):
  client.send('HTTP/1.1 200 OK')
  client.send(f'Client: {str(address)}')
  client.close()

def receive():
  while True:
    client, address = server.accept()
    thread = threading.Thread(target=handle, args=(client, address))
    thread.start()

receive()
