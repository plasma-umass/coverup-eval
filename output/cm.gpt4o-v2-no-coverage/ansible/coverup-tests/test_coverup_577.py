# file: lib/ansible/constants.py:33-40
# asked: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}
# gained: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}

import pytest
from unittest import mock
from ansible.constants import _deprecated

@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.utils.display.Display')
    return mock_display

def test_deprecated_with_display(mock_display):
    msg = "This is a deprecated message"
    version = "2.0"
    
    _deprecated(msg, version)
    
    mock_display().deprecated.assert_called_once_with(msg, version=version)

def test_deprecated_without_display(mocker):
    msg = "This is a deprecated message"
    version = "2.0"
    
    mocker.patch('ansible.utils.display.Display', side_effect=Exception("Display not available"))
    mock_stderr = mocker.patch('sys.stderr.write')
    
    _deprecated(msg, version)
    
    mock_stderr.assert_called_once_with(' [DEPRECATED] %s, to be removed in %s\n' % (msg, version))
