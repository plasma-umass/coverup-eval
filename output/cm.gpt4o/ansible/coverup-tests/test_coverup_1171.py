# file lib/ansible/module_utils/urls.py:1132-1143
# lines [1135, 1136, 1138, 1140, 1141, 1142, 1143]
# branches ['1135->1136', '1135->1138']

import pytest
from unittest.mock import Mock, patch

# Import the function getpeercert from the module
from ansible.module_utils.urls import getpeercert

# Mocking the PY3 constant to test both branches
@pytest.mark.parametrize("py3, expected_socket_attr", [
    (True, 'fp.raw._sock'),
    (False, 'fp._sock.fp._sock')
])
def test_getpeercert(py3, expected_socket_attr, mocker):
    mocker.patch('ansible.module_utils.urls.PY3', py3)
    
    # Mock response object
    mock_response = Mock()
    if py3:
        mock_socket = Mock()
        mock_response.fp.raw._sock = mock_socket
    else:
        mock_socket = Mock()
        mock_response.fp._sock.fp._sock = mock_socket

    # Test when socket has getpeercert attribute
    mock_socket.getpeercert.return_value = 'cert'
    assert getpeercert(mock_response) == 'cert'
    mock_socket.getpeercert.assert_called_once_with(False)

    # Test when socket does not have getpeercert attribute
    del mock_socket.getpeercert
    assert getpeercert(mock_response) is None

    # Clean up
    mocker.stopall()
