# file httpie/uploads.py:121-138
# lines [127]
# branches ['126->127']

import pytest
import requests
from httpie.uploads import compress_request
import zlib

@pytest.fixture
def prepared_request_with_str_body():
    req = requests.Request(method='POST', url='http://example.com', data='test string')
    return req.prepare()

def test_compress_request_with_str_body(prepared_request_with_str_body, mocker):
    mocker.patch('zlib.compressobj', return_value=zlib.compressobj())
    compress_request(prepared_request_with_str_body, always=True)
    assert 'Content-Encoding' in prepared_request_with_str_body.headers
    assert prepared_request_with_str_body.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in prepared_request_with_str_body.headers
    assert int(prepared_request_with_str_body.headers['Content-Length']) > 0
    assert isinstance(prepared_request_with_str_body.body, bytes)
