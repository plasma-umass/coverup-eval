# file lib/ansible/module_utils/urls.py:1489-1498
# lines [1489, 1498]
# branches []

import pytest
from ansible.module_utils.urls import Request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socket

# Define a simple HTTP server that will handle PUT requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PUT request received")

# Find a free port on localhost
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

# Start the HTTP server in a separate thread
@pytest.fixture(scope="module")
def start_http_server():
    port = find_free_port()
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.daemon = True
    httpd_thread.start()
    yield f"http://localhost:{port}"
    httpd.shutdown()

# Test function to improve coverage for the PUT method
def test_put_request(start_http_server):
    url = start_http_server
    request = Request()
    response = request.put(url, data=b"test data")
    assert response.code == 200
    response_data = response.read()
    assert response_data == b"PUT request received"
