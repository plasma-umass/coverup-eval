# file lib/ansible/constants.py:33-40
# lines [33, 35, 36, 37, 38, 39, 40]
# branches []

import pytest
import sys
from unittest import mock

# Assuming the _deprecated function is imported from ansible.constants
from ansible.constants import _deprecated

def test_deprecated_with_display(mocker):
    mock_display = mocker.patch('ansible.utils.display.Display')
    _deprecated("test message", "2.0")
    mock_display().deprecated.assert_called_once_with("test message", version="2.0")

def test_deprecated_without_display(mocker):
    mocker.patch('ansible.utils.display.Display', side_effect=Exception("Import error"))
    mock_stderr = mocker.patch('sys.stderr.write')
    _deprecated("test message", "2.0")
    mock_stderr.assert_called_once_with(' [DEPRECATED] test message, to be removed in 2.0\n')
