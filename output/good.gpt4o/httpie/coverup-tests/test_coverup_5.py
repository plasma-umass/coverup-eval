# file httpie/models.py:5-40
# lines [5, 6, 8, 9, 11, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 30, 32, 34, 35, 37, 38, 39, 40]
# branches ['38->39', '38->40']

import pytest
from httpie.models import HTTPMessage

class MockOrig:
    def __init__(self, headers):
        self.headers = headers

def test_http_message_content_type_str():
    headers = {'Content-Type': 'text/html'}
    orig = MockOrig(headers)
    message = HTTPMessage(orig)
    assert message.content_type == 'text/html'

def test_http_message_content_type_bytes():
    headers = {'Content-Type': b'text/html'}
    orig = MockOrig(headers)
    message = HTTPMessage(orig)
    assert message.content_type == 'text/html'

def test_http_message_not_implemented_methods():
    headers = {'Content-Type': 'text/html'}
    orig = MockOrig(headers)
    message = HTTPMessage(orig)
    
    with pytest.raises(NotImplementedError):
        list(message.iter_body(1024))
    
    with pytest.raises(NotImplementedError):
        list(message.iter_lines(1024))
    
    with pytest.raises(NotImplementedError):
        _ = message.headers
    
    with pytest.raises(NotImplementedError):
        _ = message.encoding
    
    with pytest.raises(NotImplementedError):
        _ = message.body
