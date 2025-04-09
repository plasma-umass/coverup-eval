# file: lib/ansible/cli/console.py:439-442
# asked: {"lines": [439, 440, 441, 442], "branches": []}
# gained: {"lines": [439, 440, 441, 442], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.plugins.loader import fragment_loader

@pytest.fixture
def mock_module_loader():
    with patch('ansible.plugins.loader.module_loader.find_plugin') as mock:
        yield mock

@pytest.fixture
def mock_plugin_docs():
    with patch('ansible.utils.plugin_docs.get_docstring') as mock:
        yield mock

def test_module_args(mock_module_loader, mock_plugin_docs):
    # Arrange
    args = MagicMock()
    cli = ConsoleCLI(args)
    module_name = 'test_module'
    mock_module_loader.return_value = 'path/to/test_module'
    mock_plugin_docs.return_value = (
        {'options': {'option1': {}, 'option2': {}}},
        'plainexamples',
        'returndocs',
        'metadata'
    )

    # Act
    result = cli.module_args(module_name)

    # Assert
    mock_module_loader.assert_called_once_with(module_name)
    mock_plugin_docs.assert_called_once_with('path/to/test_module', fragment_loader, is_module=True)
    assert result == ['option1', 'option2']
