import threading
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', int(os.getenv('PORT', '80'))))
server.listen()

def getStatusMessage(status):
  if status == '200':
    return 'OK'
  if status == '404':
    return 'NOT FOUND'
  return 'ERROR'

def getHTTPString(s = ''):
  return str(s + '\r\n').encode('ascii')

def getFirstLine(status):
  message = getStatusMessage(status)
  return getHTTPString(f'HTTP/1.1 {status} {message}')

def getContentType(type):
  return getHTTPString(f'Content-Type: {type}')

def getRequestString(client):
  message = (client.recv(1024).decode('ascii'))
  print(f'Message: {message}')
  return f''

def getResponseString(request):
  s = getFirstLine('200')
  s += getHTTPString()
  s += getHTTPString(request)
  return s

def handle(client, address):
  request = getRequestString(client)
  print(request)

  client.send(getResponseString(request))
  client.close()

def receive():
  while True:
    client, address = server.accept()
    thread = threading.Thread(target=handle, args=(client, address))
    thread.start()

receive()
