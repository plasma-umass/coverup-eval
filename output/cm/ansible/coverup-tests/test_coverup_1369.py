# file lib/ansible/galaxy/api.py:184-221
# lines [195, 196, 206]
# branches ['205->206']

import json
import pytest
from ansible.galaxy.api import GalaxyError
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text, to_native
from unittest.mock import MagicMock

class MockHTTPError:
    def __init__(self, code, reason, url, read_data=None):
        self.code = code
        self.reason = reason
        self.url = url
        self.read_data = read_data or b''

    def read(self):
        return self.read_data

    def geturl(self):
        return self.url

@pytest.fixture
def mock_http_error_v2():
    return MockHTTPError(404, 'Not Found', 'http://example.com/api/v2/', read_data=b'{"message": "Not found", "code": "NF"}')

@pytest.fixture
def mock_http_error_v3_no_errors():
    return MockHTTPError(500, 'Server Error', 'http://example.com/api/v3/', read_data=b'{"errors": []}')

@pytest.fixture
def mock_http_error_v3_attribute_error():
    return MockHTTPError(500, 'Server Error', 'http://example.com/api/v3/', read_data=b'not a valid json')

def test_galaxy_error_v2(mock_http_error_v2):
    with pytest.raises(GalaxyError) as exc_info:
        raise GalaxyError(mock_http_error_v2, "Error occurred")
    assert exc_info.value.http_code == 404
    assert "Not found" in exc_info.value.message
    assert "NF" in exc_info.value.message

def test_galaxy_error_v3_no_errors(mock_http_error_v3_no_errors):
    with pytest.raises(GalaxyError) as exc_info:
        raise GalaxyError(mock_http_error_v3_no_errors, "Error occurred")
    assert exc_info.value.http_code == 500
    assert "Server Error" in exc_info.value.message
    assert "Unknown" in exc_info.value.message

def test_galaxy_error_v3_attribute_error(mock_http_error_v3_attribute_error):
    with pytest.raises(GalaxyError) as exc_info:
        raise GalaxyError(mock_http_error_v3_attribute_error, "Error occurred")
    assert exc_info.value.http_code == 500
    assert "Server Error" in exc_info.value.message
    assert "Unknown" in exc_info.value.message
