# file lib/ansible/module_utils/urls.py:1500-1509
# lines [1500, 1509]
# branches []

import pytest
from ansible.module_utils.urls import Request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socket

# Define a simple HTTP request handler that can handle PATCH requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_PATCH(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Patch request received")

# Find a free port on localhost
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

# Start a simple HTTP server in a separate thread
@pytest.fixture(scope="module")
def start_http_server():
    port = find_free_port()
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    yield f"http://localhost:{port}"
    server.shutdown()

# Test function to cover the patch method in the Request class
def test_request_patch(start_http_server):
    url = start_http_server
    request = Request()
    response = request.patch(url)
    assert response.code == 200
    response_body = response.read()
    assert response_body == b"Patch request received"
