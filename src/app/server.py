import threading
import socket
import os

def listen(port = 80):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.1', port))
  server.listen()
  accept(server)

def accept(server):
  while True:
    client, _ = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

def handle(client):
  request = getRequestString(client)
  print(request)

  client.send(getResponseString(request))
  client.close()

def getRequestString(client):
  return str(client.recv(1024).decode('ascii'))

def getResponseString(request):
  s = getFirstLine('200')
  s += getContentType('text/html')
  s += getHTTPString()
  s += getHTTPString(request)
  return s

def getHTTPString(s = ''):
  return str(s + '\r\n').encode('ascii')

def getFirstLine(status):
  message = getStatusMessage(status)
  return getHTTPString(f'HTTP/1.1 {status} {message}')

def getStatusMessage(status):
  if status == '200':
    return 'OK'
  if status == '404':
    return 'NOT FOUND'
  return 'ERROR'

def getContentType(type):
  return getHTTPString(f'Content-Type: {type}')

