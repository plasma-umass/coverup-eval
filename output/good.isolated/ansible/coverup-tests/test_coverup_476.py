# file lib/ansible/module_utils/urls.py:1132-1143
# lines [1132, 1135, 1136, 1138, 1140, 1141, 1142, 1143]
# branches ['1135->1136', '1135->1138']

import pytest
from ansible.module_utils.urls import getpeercert
from unittest.mock import MagicMock

class MockSocket:
    def getpeercert(self, binary_form=False):
        if binary_form:
            return b"binary certificate"
        else:
            return "certificate"

@pytest.fixture
def mock_response():
    mock_socket = MockSocket()
    mock_fp = MagicMock(raw=MagicMock(_sock=mock_socket))
    mock_response = MagicMock(fp=mock_fp)
    return mock_response

def test_getpeercert_with_binary_form(mock_response):
    binary_certificate = getpeercert(mock_response, binary_form=True)
    assert binary_certificate == b"binary certificate"

def test_getpeercert_without_binary_form(mock_response):
    certificate = getpeercert(mock_response, binary_form=False)
    assert certificate == "certificate"

def test_getpeercert_attribute_error(mock_response):
    mock_socket = MagicMock()
    mock_socket.getpeercert.side_effect = AttributeError
    mock_fp = MagicMock(raw=MagicMock(_sock=mock_socket))
    mock_response_with_error = MagicMock(fp=mock_fp)
    certificate = getpeercert(mock_response_with_error)
    assert certificate is None
