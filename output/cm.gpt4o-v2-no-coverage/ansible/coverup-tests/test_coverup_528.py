# file: lib/ansible/module_utils/urls.py:1132-1143
# asked: {"lines": [1132, 1135, 1136, 1138, 1140, 1141, 1142, 1143], "branches": [[1135, 1136], [1135, 1138]]}
# gained: {"lines": [1132, 1135, 1136, 1140, 1141, 1142, 1143], "branches": [[1135, 1136]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.urls import getpeercert
from ansible.module_utils.six import PY3

@pytest.fixture
def mock_response_py3():
    mock_socket = Mock()
    mock_socket.getpeercert.return_value = "cert_py3"
    mock_raw = Mock()
    mock_raw._sock = mock_socket
    mock_fp = Mock()
    mock_fp.raw = mock_raw
    mock_response = Mock()
    mock_response.fp = mock_fp
    return mock_response

@pytest.fixture
def mock_response_py2():
    mock_socket = Mock()
    mock_socket.getpeercert.return_value = "cert_py2"
    mock_fp_sock = Mock()
    mock_fp_sock._sock = mock_socket
    mock_fp = Mock()
    mock_fp._sock = mock_fp_sock
    mock_response = Mock()
    mock_response.fp = mock_fp
    return mock_response

def test_getpeercert_py3(mock_response_py3):
    if PY3:
        cert = getpeercert(mock_response_py3)
        assert cert == "cert_py3"

def test_getpeercert_py2(mock_response_py2):
    if not PY3:
        cert = getpeercert(mock_response_py2)
        assert cert == "cert_py2"

def test_getpeercert_not_https():
    mock_socket = Mock()
    mock_socket.getpeercert.side_effect = AttributeError
    mock_raw = Mock()
    mock_raw._sock = mock_socket
    mock_fp = Mock()
    mock_fp.raw = mock_raw if PY3 else Mock(_sock=mock_socket)
    mock_response = Mock()
    mock_response.fp = mock_fp
    cert = getpeercert(mock_response)
    assert cert is None
