#!/usr/bin/env python3
"""Develop a simple API using Python with the `http.server` module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """gérer les différents endpoint avec code 200"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # str en bytes

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John',
                'age': 30,
                'city': 'New York'
            }
            self.wfile.write(bytes(json.dumps(data), "utf8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            status = (b"OK")
            self.wfile.write(bytes(json.dumps(status), "utf8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf8"))

        else:
            """gérer les endpoints failed"""
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Endpoint not found')


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', PORT), MyHandler)
    print(f"Server running on localhost:{PORT}")
    httpd.serve_forever()
