# file lib/ansible/cli/console.py:147-158
# lines []
# branches ['149->154', '151->150', '156->155']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.module_utils import basic

@pytest.fixture
def mock_context(mocker):
    context_mock = mocker.patch('ansible.cli.console.context')
    context_mock.CLIARGS = {'module_path': ['/fake/path1', None, '/fake/path2']}
    return context_mock

@pytest.fixture
def mock_module_loader(mocker):
    module_loader_mock = mocker.patch('ansible.cli.console.module_loader')
    module_loader_mock._get_paths.return_value = ['/fake/path1', None, '/fake/path2']
    return module_loader_mock

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_list_modules(mock_context, mock_module_loader, console_cli):
    mock_module_loader.add_directory = mock.Mock()
    console_cli._find_modules_in_path = mock.Mock(return_value={'module1', 'module2'})

    modules = console_cli.list_modules()

    # Assertions to verify the correct paths were added and modules found
    mock_module_loader.add_directory.assert_any_call('/fake/path1')
    mock_module_loader.add_directory.assert_any_call('/fake/path2')
    console_cli._find_modules_in_path.assert_any_call('/fake/path1')
    console_cli._find_modules_in_path.assert_any_call('/fake/path2')
    assert modules == {'module1', 'module2'}

    # Clean up
    mock_context.stop()
    mock_module_loader.stop()
