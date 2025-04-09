# file: lib/ansible/cli/console.py:439-442
# asked: {"lines": [439, 440, 441, 442], "branches": []}
# gained: {"lines": [439, 440, 441, 442], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.plugins.loader import module_loader, fragment_loader
from ansible.utils.plugin_docs import get_docstring

@pytest.fixture
def mock_module_loader(mocker):
    mock = mocker.patch('ansible.plugins.loader.module_loader.find_plugin')
    mock.return_value = 'mock_path'
    return mock

@pytest.fixture
def mock_get_docstring(mocker):
    mock = mocker.patch('ansible.utils.plugin_docs.get_docstring')
    mock.return_value = ({
        'options': {
            'option1': {},
            'option2': {}
        }
    }, None, None, None)
    return mock

def test_module_args(mock_module_loader, mock_get_docstring):
    cli = ConsoleCLI(args=['test'])
    result = cli.module_args('mock_module')
    assert result == ['option1', 'option2']
    mock_module_loader.assert_called_once_with('mock_module')
    mock_get_docstring.assert_called_once_with('mock_path', fragment_loader, is_module=True)
