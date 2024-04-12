# file lib/ansible/cli/console.py:439-442
# lines [439, 440, 441, 442]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.plugins.loader import module_loader
from ansible.utils.plugin_docs import get_docstring

# Mocking the necessary parts to test the module_args function
@pytest.fixture
def mock_module_loader(mocker):
    mocker.patch('ansible.plugins.loader.module_loader.find_plugin', return_value='/path/to/module')
    return module_loader

@pytest.fixture
def mock_plugin_docs(mocker):
    docstring = {
        'options': {
            'option1': 'description1',
            'option2': 'description2',
        }
    }
    mocker.patch('ansible.utils.plugin_docs.get_docstring', return_value=(docstring, None, None, None))
    return get_docstring

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    return ConsoleCLI(args=[])

def test_module_args(mock_module_loader, mock_plugin_docs, console_cli):
    module_name = 'test_module'
    args = console_cli.module_args(module_name)
    assert args == ['option1', 'option2']
