# file thefuck/shells/generic.py:42-44
# lines [42, 43, 44]
# branches []

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import patch

def test_instant_mode_alias(mocker):
    mock_warn = mocker.patch('thefuck.shells.generic.warn')
    generic_shell = Generic()
    alias_name = 'test_alias'
    with patch.object(Generic, 'app_alias', return_value='mocked_app_alias') as mock_app_alias:
        result = generic_shell.instant_mode_alias(alias_name)
        mock_app_alias.assert_called_once_with(alias_name)
        mock_warn.assert_called_once_with("Instant mode not supported by your shell")
        assert result == 'mocked_app_alias'
