# file lib/ansible/cli/console.py:439-442
# lines [439, 440, 441, 442]
# branches []

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.plugins.loader import module_loader, fragment_loader
from ansible.utils.plugin_docs import get_docstring

@pytest.fixture
def mock_module_loader(mocker):
    return mocker.patch('ansible.plugins.loader.module_loader.find_plugin')

@pytest.fixture
def mock_get_docstring(mocker):
    return mocker.patch('ansible.utils.plugin_docs.get_docstring')

def test_module_args(mock_module_loader, mock_get_docstring):
    # Arrange
    mock_module_loader.return_value = 'fake_path'
    mock_get_docstring.return_value = (
        {'options': {'option1': {}, 'option2': {}}},
        None,
        None,
        None
    )
    cli = ConsoleCLI(args=['fake_arg'])

    # Act
    result = cli.module_args('fake_module')

    # Assert
    assert result == ['option1', 'option2']
    mock_module_loader.assert_called_once_with('fake_module')
    mock_get_docstring.assert_called_once_with('fake_path', fragment_loader, is_module=True)
