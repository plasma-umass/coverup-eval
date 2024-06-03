# file lib/ansible/cli/console.py:147-158
# lines [147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158]
# branches ['149->150', '149->154', '150->151', '150->154', '151->150', '151->152', '155->156', '155->158', '156->155', '156->157']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.module_utils import basic

@pytest.fixture
def mock_context(mocker):
    context_mock = mocker.patch('ansible.cli.console.context')
    context_mock.CLIARGS = {'module_path': ['/fake/path']}
    return context_mock

@pytest.fixture
def mock_module_loader(mocker):
    module_loader_mock = mocker.patch('ansible.cli.console.module_loader')
    module_loader_mock._get_paths.return_value = ['/fake/path']
    module_loader_mock.add_directory = mock.Mock()
    return module_loader_mock

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    return ConsoleCLI(args=[])

def test_list_modules(mock_context, mock_module_loader, console_cli):
    with mock.patch.object(console_cli, '_find_modules_in_path', return_value={'fake_module'}):
        modules = console_cli.list_modules()
        assert 'fake_module' in modules
        mock_module_loader.add_directory.assert_called_with('/fake/path')
        mock_module_loader._get_paths.assert_called_once()
        console_cli._find_modules_in_path.assert_called_with('/fake/path')
