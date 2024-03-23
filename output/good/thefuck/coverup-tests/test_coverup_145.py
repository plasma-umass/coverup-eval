# file thefuck/shells/generic.py:140-147
# lines [142, 143, 144, 145, 146, 147]
# branches []

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import Mock
from pytest import warns

class TestGenericShell:
    @pytest.fixture
    def shell(self, mocker):
        mocker.patch('thefuck.shells.generic.warn')
        generic_shell = Generic()
        generic_shell.friendly_name = 'TestShell'
        return generic_shell

    def test_info_with_version(self, shell, mocker):
        # Mock _get_version to return a specific version
        mocker.patch.object(shell, '_get_version', return_value='1.0.0')
        assert shell.info() == 'TestShell 1.0.0'

    def test_info_with_exception(self, shell, mocker):
        # Mock _get_version to raise an exception
        mocker.patch.object(shell, '_get_version', side_effect=Exception('Test exception'))
        # Mock warn to capture the warning
        mock_warn = mocker.patch('thefuck.shells.generic.warn')
        assert shell.info() == 'TestShell'
        # Check that warn was called with the expected message
        mock_warn.assert_called_once_with(u'Could not determine shell version: Test exception')
