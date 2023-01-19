import os
import server

port=int(os.getenv('PORT', '80'))
server.listen(port)
