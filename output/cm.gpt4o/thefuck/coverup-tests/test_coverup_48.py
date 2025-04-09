# file thefuck/shells/generic.py:140-147
# lines [140, 142, 143, 144, 145, 146, 147]
# branches []

import pytest
from unittest.mock import patch, Mock
from thefuck.shells.generic import Generic
from thefuck.utils import warn

@pytest.fixture
def generic_shell():
    return Generic()

def test_info_success(generic_shell):
    with patch.object(generic_shell, '_get_version', return_value='1.0.0'):
        generic_shell.friendly_name = 'TestShell'
        result = generic_shell.info()
        assert result == 'TestShell 1.0.0'

def test_info_failure(generic_shell, mocker):
    mocker.patch.object(generic_shell, '_get_version', side_effect=Exception('Test error'))
    mock_warn = mocker.patch('thefuck.shells.generic.warn')
    generic_shell.friendly_name = 'TestShell'
    result = generic_shell.info()
    mock_warn.assert_called_once_with('Could not determine shell version: Test error')
    assert result == 'TestShell'
