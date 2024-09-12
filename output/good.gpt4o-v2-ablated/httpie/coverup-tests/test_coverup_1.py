# file: httpie/models.py:5-40
# asked: {"lines": [5, 6, 8, 9, 11, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 30, 32, 34, 35, 37, 38, 39, 40], "branches": [[38, 39], [38, 40]]}
# gained: {"lines": [5, 6, 8, 9, 11, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 30, 32, 34, 35, 37, 38, 39, 40], "branches": [[38, 39], [38, 40]]}

import pytest
from httpie.models import HTTPMessage

class MockOrig:
    def __init__(self, headers):
        self.headers = headers

def test_http_message_init():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    assert message._orig == orig

def test_http_message_iter_body():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    with pytest.raises(NotImplementedError):
        list(message.iter_body(1024))

def test_http_message_iter_lines():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    with pytest.raises(NotImplementedError):
        list(message.iter_lines(1024))

def test_http_message_headers():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    with pytest.raises(NotImplementedError):
        _ = message.headers

def test_http_message_encoding():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    with pytest.raises(NotImplementedError):
        _ = message.encoding

def test_http_message_body():
    orig = MockOrig(headers={})
    message = HTTPMessage(orig)
    with pytest.raises(NotImplementedError):
        _ = message.body

def test_http_message_content_type_str():
    headers = {'Content-Type': 'text/html'}
    orig = MockOrig(headers=headers)
    message = HTTPMessage(orig)
    assert message.content_type == 'text/html'

def test_http_message_content_type_bytes():
    headers = {'Content-Type': b'text/html'}
    orig = MockOrig(headers=headers)
    message = HTTPMessage(orig)
    assert message.content_type == 'text/html'

def test_http_message_content_type_missing():
    headers = {}
    orig = MockOrig(headers=headers)
    message = HTTPMessage(orig)
    assert message.content_type == ''
