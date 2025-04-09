# file thefuck/entrypoints/not_configured.py:19-26
# lines [19, 21, 23, 24, 25, 26]
# branches []

import os
import pytest
from unittest.mock import patch
from psutil import Process

# Assuming the function _get_shell_pid is imported from thefuck.entrypoints.not_configured
from thefuck.entrypoints.not_configured import _get_shell_pid

def test_get_shell_pid(mocker):
    # Mocking Process and its methods
    mock_process = mocker.patch('thefuck.entrypoints.not_configured.Process')
    mock_proc_instance = mock_process.return_value
    mock_parent = mock_proc_instance.parent

    # Test case where parent() returns a process with a pid attribute
    mock_parent.return_value.pid = 1234
    assert _get_shell_pid() == 1234

    # Test case where parent() raises a TypeError and parent has a pid attribute
    mock_parent.side_effect = TypeError
    mock_proc_instance.parent.pid = 5678
    assert _get_shell_pid() == 5678
