# file tornado/netutil.py:374-386
# lines [374, 375, 382, 383, 384, 385, 386]
# branches ['384->385', '384->386']

import socket
import pytest
from unittest import mock

# Assuming the _resolve_addr function is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named `netutil`.
from tornado.netutil import _resolve_addr

def test_resolve_addr(mocker):
    # Mocking socket.getaddrinfo to control its output
    mock_getaddrinfo = mocker.patch('socket.getaddrinfo')
    
    # Sample data to be returned by the mock
    mock_getaddrinfo.return_value = [
        (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80)),
        (socket.AF_INET6, socket.SOCK_STREAM, 6, '', ('::1', 80)),
    ]
    
    # Call the function with test data
    result = _resolve_addr('localhost', 80)
    
    # Verify the result
    assert result == [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
    ]
    
    # Ensure the mock was called with the expected parameters
    mock_getaddrinfo.assert_called_once_with('localhost', 80, socket.AF_UNSPEC, socket.SOCK_STREAM)

# Note: pytest-mock is used to mock socket.getaddrinfo and ensure no real network calls are made.
