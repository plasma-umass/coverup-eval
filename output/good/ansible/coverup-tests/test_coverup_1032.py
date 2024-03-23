# file lib/ansible/module_utils/urls.py:1458-1466
# lines [1458, 1466]
# branches []

import pytest
from ansible.module_utils.urls import Request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Define a simple HTTP server that can handle OPTIONS request
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

# Function to start the HTTP server in a separate thread
def run_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 0)  # Bind to an available port provided by the OS
    httpd = server_class(server_address, handler_class)
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.daemon = True
    httpd_thread.start()
    return httpd

# Test function to check the OPTIONS method of the Request class
@pytest.fixture(scope="module")
def server():
    server = run_server()
    yield server
    server.shutdown()

def test_request_options_method(server):
    host, port = server.server_address
    url = f'http://{host}:{port}'
    request = Request()

    # Perform an OPTIONS request
    response = request.options(url)

    # Check that the response is an HTTPResponse object and the status code is 200
    assert hasattr(response, 'code')
    assert response.code == 200

# Run the test
def test_options_request(server):
    test_request_options_method(server)
