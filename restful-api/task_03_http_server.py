#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """gérer les différents endpoint avec code 200"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # str en bytes

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John Doe',
                'age': 30,
                'city': 'New York'
            }
            self.wfile.write(bytes(json.dumps(data), "utf8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                'status': 'OK'
            }
            self.wfile.write(bytes(json.dumps(status), "utf8"))

        else:
            """gérer les endpoints failed"""
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not found')


httpd = HTTPServer(('localhost', PORT), MyHandler)
print(f"Server running on localhost:{PORT}")
httpd.serve_forever()
