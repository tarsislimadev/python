import threading
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', int(os.getenv('PORT', '80'))))
server.listen()

class Request:
  def __init__(self, chunk):
    self.method = ''
    self.pathname = ''
    self.query = ''
    self.headers = []
    self.body = ''

class ResponseObject:
  def __init__(self, json = {}) -> None:
    self.status = 'ok'
    self.message = ''
    self.data = ''

class Response:
  def __init__(self, request):
    self.request = request
    self.status = 200
    self.body = ResponseObject()

  def __str__(self):
    return f''

def start():
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

start()
