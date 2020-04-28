import http.server as BaseHTTPServer
import os
import shutil
import sys
from urllib.parse import unquote

from certificate_generator import certificat

FILEPATH = "new_certificate.png"


class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        name = unquote(self.path)
        name = name.replace("/", "")
        certificat(name)
        with open(FILEPATH, 'rb') as f:
            self.send_header("Content-Type", 'application/octet-stream')
            self.send_header("Content-Disposition", 'attachment; filename="{}"'.format(os.path.basename(FILEPATH)))
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs.st_size))
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)


def run_server(HandlerClass=SimpleHTTPRequestHandler,
               ServerClass=BaseHTTPServer.HTTPServer,
               protocol="HTTP/1.0"):
    if sys.argv[2:]:
        port = int(sys.argv[2])
    else:
        port = 8000
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = BaseHTTPServer.HTTPServer(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on {0[0]} port {0[1]} ... {1}".format(sa, FILEPATH))
    httpd.serve_forever()