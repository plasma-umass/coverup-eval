# file: lib/ansible/module_utils/urls.py:1132-1143
# asked: {"lines": [1135, 1136, 1138, 1140, 1141, 1142, 1143], "branches": [[1135, 1136], [1135, 1138]]}
# gained: {"lines": [1135, 1136, 1138, 1140, 1141, 1142, 1143], "branches": [[1135, 1136], [1135, 1138]]}

import pytest
import sys
from unittest.mock import Mock, MagicMock

# Mocking PY3 to simulate both Python 2 and Python 3 environments
@pytest.mark.parametrize("py3_value", [True, False])
def test_getpeercert(py3_value, monkeypatch):
    # Mocking the PY3 variable
    monkeypatch.setattr("ansible.module_utils.six.PY3", py3_value)
    
    # Creating a mock response object
    response = Mock()
    
    if py3_value:
        # Simulating Python 3 response structure
        response.fp.raw._sock = MagicMock()
        mock_socket = response.fp.raw._sock
    else:
        # Simulating Python 2 response structure
        response.fp._sock.fp._sock = MagicMock()
        mock_socket = response.fp._sock.fp._sock
    
    # Mocking the getpeercert method
    mock_socket.getpeercert.return_value = "mock_certificate"
    
    from ansible.module_utils.urls import getpeercert
    
    # Calling the function and asserting the result
    assert getpeercert(response) == "mock_certificate"
    
    # Ensuring getpeercert was called with the correct parameters
    mock_socket.getpeercert.assert_called_with(False)

    # Simulating AttributeError to test the exception handling
    mock_socket.getpeercert.side_effect = AttributeError
    assert getpeercert(response) is None
