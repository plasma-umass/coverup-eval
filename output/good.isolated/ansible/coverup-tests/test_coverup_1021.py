# file lib/ansible/module_utils/urls.py:1511-1519
# lines [1511, 1519]
# branches []

import pytest
from ansible.module_utils.urls import Request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socket


# Define a simple HTTP server that can handle DELETE requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Deleted")

# Find a free port on localhost
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

# Start the HTTP server in a separate thread
@pytest.fixture(scope="module")
def http_server():
    port = find_free_port()
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    yield server, port
    server.shutdown()

# Test function to improve coverage for the delete method
def test_delete_request(http_server):
    server, port = http_server
    url = f'http://localhost:{port}/'
    request = Request()

    # Perform the DELETE request
    response = request.delete(url)

    # Check that the response is as expected
    assert response.code == 200
    assert response.read() == b"Deleted"
