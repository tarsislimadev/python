import os
import http.server as server

port=int(os.getenv('PORT', '80'))
server.listen(port)
